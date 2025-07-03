from flask import Flask, render_template, request, jsonify
from datetime import datetime
import hashlib
import json
import os

from transformers import pipeline

app = Flask(__name__)

# Initialize emotion detection pipeline
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=None)

# Create folder to store entries if not exists
if not os.path.exists("entries"):
    os.makedirs("entries")

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save_entry():
    data = request.get_json()
    entry_text = data.get("entry", "")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Predict emotions
    results = emotion_classifier(entry_text)[0]
    # Get emotion with highest score
    top_emotion = max(results, key=lambda x: x['score'])
    emotion_label = top_emotion['label']
    confidence = round(top_emotion['score'] * 100, 2)

    entry_data = {
        "text": entry_text,
        "timestamp": timestamp,
        "hash": generate_hash(entry_text + timestamp),
        "emotion": emotion_label,
        "confidence": confidence
    }

    filename = f"entries/{timestamp.replace(':', '-')}.json"
    with open(filename, "w") as f:
        json.dump(entry_data, f, indent=4)

    return jsonify({
        "message": "Entry saved successfully!",
        "hash": entry_data["hash"],
        "emotion": emotion_label,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)
