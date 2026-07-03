import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def get_response():
    user_msg = request.json.get("message")
    if not user_msg:
        return jsonify({"error": "No message provided"}), 400
    try:
        response = chat.send_message(user_msg)
        return jsonify({"reply": response.text})
    except Exception as e:
        import traceback
        traceback.print_exc
        print(e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)