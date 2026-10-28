Writing
🇮🇳 JanSathi AI
AI-Powered Government Schemes Information Assistant
JanSathi AI is an AI-powered chatbot designed to help Indian citizens discover and understand government welfare schemes through simple, conversational interactions.
Our goal is to make government scheme information easier to access, understand and verify using artificial intelligence and a user-friendly web interface.
🌟 Features
🤖 AI Chatbot: Ask questions about government schemes in natural language.
🏛️ Government Schemes Directory: Browse available scheme information.
📋 Scheme Details: Explore descriptions, benefits and eligibility information where available.
🔗 Official Government Sources: Visit official portals to verify scheme information.
🌐 Web-Based Interface: Access the application through a browser.
☁️ Cloud Deployment: Backend and frontend are hosted online.
🔐 API Key Security: AI credentials are configured on the backend rather than exposed in frontend code.
🎯 Problem Statement
Many citizens find it difficult to discover government welfare schemes and understand their benefits, eligibility conditions and application procedures.
JanSathi AI aims to reduce this information gap by providing a simple conversational interface for exploring government scheme information.
💡 Our Solution
JanSathi AI combines a web interface, a Python FastAPI backend and an AI-powered question-answering feature.
Users can ask questions about government schemes and receive helpful guidance. Users should verify important details, eligibility and application requirements through official government portals.
🛠️ Technology Stack
Frontend: HTML, CSS and JavaScript
Backend: Python and FastAPI
AI Integration: Google AI API
Hosting: Render
Version Control: Git and GitHub
Open-weight AI model: The project is intended to use Google's Gemma model. The exact model identifier should be verified in the backend configuration before claiming that the deployed chatbot uses Gemma.
🚀 Live Project Links
Live Backend: https://jansathi-ai-m5q4.onrender.com
API Documentation: https://jansathi-ai-m5q4.onrender.com/docs
Government Schemes API: https://jansathi-ai-m5q4.onrender.com/schemes
Government Scheme Sources API: https://jansathi-ai-m5q4.onrender.com/schemes/sources
Live Frontend Website: Add your Render Static Site URL here.
GitHub Repository: Add your actual GitHub repository URL here.
🏛️ Official Government Sources
The following official portals can be used to verify government scheme information.
National Portal of India: https://www.india.gov.in/
Government Schemes Directory: https://www.india.gov.in/my-government/schemes
myScheme — Government Schemes Discovery Portal: https://www.myscheme.gov.in/
PM-KISAN Official Portal: https://pmkisan.gov.in/
Ayushman Bharat PM-JAY: https://pmjay.gov.in/about/pmjay
National Health Authority: https://nha.gov.in/
Scheme details, eligibility rules, benefits and application procedures can change. Always consult the relevant official portal for the latest information.
📋 Prerequisites
Python 3.10 or a compatible supported Python version
pip
Git
A Google AI API key if required by the configured AI integration
💻 Local Setup Guide
1. Clone the repository
Replace YOUR_GITHUB_REPOSITORY_URL with the actual URL of this repository.
git clone YOUR_GITHUB_REPOSITORY_URL
cd jansathi-ai
2. Create a virtual environment
Windows PowerShell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file in the backend project directory.
Add the environment variable name expected by your backend code. For example:
GOOGLE_API_KEY=your_api_key_here
If your code uses GEMINI_API_KEY or another variable name, use that exact name instead.
Security warning: Never upload your real API key to GitHub. Keep .env excluded through .gitignore. Configure production secrets in your hosting provider's environment settings.
5. Run the backend
python -m uvicorn main:app --reload
Open the API documentation:
http://127.0.0.1:8000/docs
Use the port configured by your application if it differs from 8000.
6. Open the frontend
Open index.html in a browser or deploy it as a static website.
Ensure the frontend API URL points to the correct backend endpoint.
🧪 Testing the API
Visit the live API documentation:
https://jansathi-ai-m5q4.onrender.com/docs
Available endpoints include:
GET / — Backend status
GET /schemes — Government schemes information
GET /schemes/sources — Scheme sources
POST /chat — Ask the AI chatbot a question
The /chat endpoint expects a JSON request containing a question field, according to the current API schema.
Example:
{
  "question": "PM Kisan Yojana kya hai?"
}
🔐 Security and Responsible AI
Keep API keys in environment variables.
Never commit passwords, secrets or API keys to GitHub.
Verify important scheme information against official government sources.
Do not treat AI-generated answers as official government decisions.
Avoid sharing sensitive personal information in chatbot conversations.
🌍 Why Does Open Innovation Matter?
Open innovation allows developers, students and communities to collaborate, exchange ideas and improve solutions to real-world problems.
JanSathi AI can benefit from community contributions, verified government information, accessibility improvements and feedback from users.
By sharing code and encouraging collaboration, the project aims to make government scheme information easier to discover and understand.
🤝 Contributing
Contributions and suggestions are welcome.
Fork the repository.
Create a feature branch.
Make your changes.
Test your changes.
Submit a pull request explaining the improvement.
Please do not include API keys, passwords or other secrets in contributions.
🗺️ Future Improvements
Expand the scheme database using verified official information.
Improve Hindi and other Indian-language support.
Provide clearer citations for AI-generated answers.
Improve mobile accessibility and user experience.
Add automated tests and better error handling.
Verify and document the exact Gemma model used.
Collect community feedback to improve the project.
📄 License
Choose and add an appropriate open-source license, such as the MIT License, before distributing the project under that license.
🙌 Acknowledgements
Thanks to the open-source community, public government information portals and developers working to make technology more accessible.
JanSathi AI — Making Government Scheme Information Easier to Access.
