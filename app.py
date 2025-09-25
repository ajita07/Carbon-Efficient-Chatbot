from flask import Flask, request, jsonify, render_template
from chatbot import CarbonEfficientChatbot
from tracker import CarbonTracker
import os

app = Flask(__name__)

# ✅ Get API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

chatbot = CarbonEfficientChatbot(api_key=GROQ_API_KEY)
tracker = CarbonTracker()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    tracker.start()
    reply = chatbot.get_reply(user_input)
    emissions = tracker.stop()

    print(f"DEBUG - Emissions value: {emissions}")
    print(f"DEBUG - Emissions type: {type(emissions)}")

    return jsonify({"reply": reply, "emissions": emissions})

