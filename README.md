# Gemini AI Chatbot

A conversational AI chatbot built using Python, Flask, and Google's Gemini API. Unlike rule-based chatbots, this uses a generative LLM to produce dynamic, context-aware responses.

## Tech Stack
- Python
- Flask
- Google Generative AI SDK (Gemini API)
- HTML / CSS / JavaScript (frontend)

## Features
- Real-time chat interface
- Maintains conversation context/history
- Simple REST API (`/chat` endpoint)
- Easy to deploy on Render/Railway/PythonAnywhere

## Setup Instructions

1. Clone/extract the project and open the folder.

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Get a free Gemini API key from [Google AI Studio](https://aistudio.google.com).

5. Rename `.env.example` to `.env` and add your key:
   ```
   GEMINI_API_KEY=your_actual_key_here
   ```

6. Run the app:
   ```
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

## Deployment
Push to GitHub, then deploy on [Render](https://render.com):
- Build command: `pip install -r requirements.txt`
- Start command: `python app.py`
- Add `GEMINI_API_KEY` as an environment variable in Render's dashboard.

## Resume Keywords
Generative AI, Google Gemini API, Python, Flask, REST API, Conversational AI, Chatbot Development, Prompt Engineering

## Possible Extensions
- Add RAG (Retrieval Augmented Generation) with a PDF/knowledge base
- Add file upload support
- Add user authentication and chat history storage (SQLite)
- Deploy with a custom domain
# gemini-chatbot
