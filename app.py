from flask import Flask, render_template, request, jsonify
from datetime import datetime
import hashlib
import json
import os
from textblob import TextBlob

app = Flask(__name__)

# Create folder to store entries if not exists
if not os.path.exists("entries"):
    os.makedirs("entries")


def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "Happy", round(polarity * 100, 2)
    elif polarity < -0.2:
        return "Sad", round(abs(polarity) * 100, 2)
    else:
        return "Neutral", round(abs(polarity) * 100, 2)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save", methods=["POST"])
def save_entry():
    data = request.get_json()
    entry_text = data.get("entry", "")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Server-side emotion detection
    emotion, confidence = detect_emotion(entry_text)

    entry_data = {
        "text": entry_text,
        "timestamp": timestamp,
        "hash": generate_hash(entry_text + timestamp),
        "emotion": emotion,
        "confidence": confidence
    }

    filename = f"entries/{timestamp.replace(':', '-')}.json"
    with open(filename, "w") as f:
        json.dump(entry_data, f, indent=4)

    return jsonify({
        "message": "Entry saved successfully!",
        "hash": entry_data["hash"],
        "emotion": emotion,
        "confidence": confidence
    })


@app.route("/entries")
def view_entries():
    entries = []
    emotion_filter = request.args.get('emotion')
    date_filter = request.args.get('date')

    for file in os.listdir("entries"):
        if file.endswith(".json"):
            with open(os.path.join("entries", file), "r") as f:
                data = json.load(f)
                if emotion_filter and data.get("emotion", "").lower() != emotion_filter.lower():
                    continue
                if date_filter and not data.get("timestamp", "").startswith(date_filter):
                    continue
                entries.append(data)

    entries.sort(key=lambda x: x["timestamp"], reverse=True)
    return render_template("entries.html", entries=entries)



if __name__ == "__main__":
    app.run(debug=True)
