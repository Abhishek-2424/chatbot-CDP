from flask import Flask, render_template, request, jsonify
import json
import os
from chatbot import get_relevant_answer  # Import the function from chatbot.py

app = Flask(__name__)

# Load CDP Documentation Data
DATA_FILE = "scraped_data.json"  # Ensure this file contains extracted documentation data

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    response = get_relevant_answer(user_input)  # Use the function to get the response
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
