import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

load_dotenv()

app = FastAPI(title="JanSathi AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Google Gen AI client
api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key) if api_key else None

# Gemma model
MODEL_NAME = "gemma-4-26b-a4b-it"

# Government schemes data
schemes_data = [
    {
        "id": 1,
        "name": "PM Kisan Samman Nidhi",
        "category": "Agriculture",
        "description": "Eligible farmer families ko financial assistance di jati hai.",
        "eligibility": "Eligibility aur exclusions official PM-KISAN guidelines ke anusar check karein.",
        "benefits": "₹6,000 per year, 3 equal installments mein, scheme rules ke anusar.",
        "application_process": "Official portal par New Farmer Registration aur eligibility details check karein.",
        "official_source": "https://pmkisan.gov.in/"
    },
    {
        "id": 2,
        "name": "Ayushman Bharat PM-JAY",
        "category": "Health",
        "description": "Eligible beneficiaries ko empanelled hospitals mein cashless hospital treatment ki suvidha milti hai.",
        "eligibility": "Apni eligibility official portal ya authorised helpdesk se verify karein.",
        "benefits": "Eligible beneficiaries ko scheme rules ke anusar hospitalisation coverage milta hai.",
        "application_process": "Official portal par eligibility aur beneficiary services check karein.",
        "official_source": "https://pmjay.gov.in/"
    },
    {
        "id": 3,
        "name": "National Scholarship Portal",
        "category": "Education",
        "description": "Eligible students ke liye scholarship schemes ki jankari aur application services.",
        "eligibility": "Har scholarship ki eligibility, income limit aur academic conditions alag ho sakti hain.",
        "benefits": "Selected scholarship scheme ke rules ke anusar financial assistance.",
        "application_process": "Portal par scholarship details, application dates aur required documents check karein.",
        "official_source": "https://scholarships.gov.in/"
    },
    {
        "id": 4,
        "name": "MGNREGA",
        "category": "Employment",
        "description": "Rural households ke eligible adult members ko unskilled manual work ke through livelihood support dene ka programme.",
        "eligibility": "Rural households ke adult members aur applicable scheme rules ke anusar.",
        "benefits": "Eligible rural households ke liye financial year mein 100 din ke guaranteed wage employment ka statutory framework.",
        "application_process": "Gram Panchayat ya official portal par job card aur work demand process ki jankari lein.",
        "official_source": "https://nrega.dord.gov.in/MGNREGA_new/Nrega_home.aspx"
    }
]


# Chat request model
class ChatRequest(BaseModel):
    question: str


# Home API
@app.get("/")
def home():
    return {
        "message": "JanSathi AI backend is running"
    }


# All government schemes
@app.get("/schemes")
def get_schemes():
    return schemes_data


# Official sources for schemes
@app.get("/schemes/sources")
def get_scheme_sources():
    return [
        {
            "id": scheme["id"],
            "name": scheme["name"],
            "official_source": scheme["official_source"],
            "verification_status": (
                "Official source link provided; "
                "details need verification"
            )
        }
        for scheme in schemes_data
    ]


# Chatbot API using Gemma
@app.post("/chat")
def chat(request: ChatRequest):
    if not client:
        raise HTTPException(
            status_code=500,
            detail="Google API key .env file mein nahi mili."
        )

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Please enter a question."
        )

    # Scholarship questions ke liye direct fallback
    scholarship_keywords = [
        "scholarship",
        "scholarships",
        "national scholarship",
        " छात्रवृत्ति",
        "छात्रवृत्ति"
    ]

    if any(word in question.lower() for word in scholarship_keywords):
        scholarship_data = next(
            (
                scheme for scheme in schemes_data
                if scheme["id"] == 3
            ),
            None
        )

        if scholarship_data:
            fallback_answer = (
                "National Scholarship Portal par apply karne "
                "ke liye official website kholen:\n"
                "https://scholarships.gov.in/\n\n"
                "Eligibility:\n"
                + scholarship_data["eligibility"]
                + "\n\nApplication process:\n"
                + scholarship_data["application_process"]
                + "\n\nImportant: Har scholarship ki eligibility, "
                "income limit, documents aur application dates "
                "alag ho sakti hain. Latest details official "
                "portal par verify karein."
            )
        else:
            fallback_answer = (
                "Scholarship ki latest eligibility aur application "
                "details https://scholarships.gov.in/ par check karein."
            )

    else:
        fallback_answer = None

    # Google AI se jawab lene ki 2 koshish
    for attempt in range(2):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=(
                    "You are JanSathi AI. Answer in simple Hindi "
                    "or Hinglish. Keep answers clear and concise. "
                    "Use the provided government scheme data. "
                    "Never invent eligibility rules or deadlines. "
                    "Share official links when available and advise "
                    "users to verify current details on official sites.\n\n"
                    f"Scheme data: {schemes_data}\n\n"
                    f"User question: {question}"
                )
            )

            if response.text:
                return {"answer": response.text}

        except Exception as e:
            print(
                f"Gemma attempt {attempt + 1} failed: {e}"
            )

    # AI service fail hone par useful scheme information
    if fallback_answer:
        return {"answer": fallback_answer}

    raise HTTPException(
        status_code=503,
        detail=(
            "AI service abhi temporarily unavailable hai. "
            "Kripya thodi der baad dobara try karein."
        )
    )