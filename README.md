# AI ChatAssistant


A conversational AI chatbot built using Python, Flask, and Google's Gemini API. Unlike rule-based chatbots, this uses a generative LLM to produce dynamic, context-aware responses in real time.

Features


Real-time chat interface
Context-aware conversation (maintains chat history)
REST API architecture (/chat endpoint)
Secure API key handling via environment variables
Deployment-ready (Render)


Tech Stack


Backend: Python, Flask
AI Model: Google Gemini API (gemini-1.5-flash)
Frontend: HTML, CSS, JavaScript
Other: python-dotenv (environment variable management)


Project Structure

gemini-chatbot/
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

Setup Instructions


Clone the repository:


bash   git clone https://github.com/ChennojuSowmya2324/gemini-chatbot.git
   cd gemini-chatbot
   
Install dependencies:

bash   pip install -r requirements.txt


Get a free Gemini API key from Google AI Studio.
Rename .env.example to .env and add your key:


   GEMINI_API_KEY=your_actual_key_here
   
Run the app:

bash   python app.py

Open http://127.0.0.1:5000 in your browser.

Deployment

Deployed on Render:

Build Command: pip install -r requirements.txt
Start Command: python app.py
Add GEMINI_API_KEY as an environment variable in Render's dashboard.

Key Concepts Demonstrated

REST API design with Flask
Generative AI integration (LLM API calls)
Environment variable security (no hardcoded keys)
Session-based chat context handling


Future Improvements


Add RAG (Retrieval Augmented Generation) with a PDF knowledge base
Add user authentication
Store chat history in SQLite
Add file upload support


Author

Sowmya Chennoju
