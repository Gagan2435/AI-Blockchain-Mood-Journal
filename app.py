# =============================
# app.py (clean final version)
# =============================
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import hashlib
import json
import os
from textblob import TextBlob
from flask import Flask, render_template, request, jsonify, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'


# Ensure entries folder exists
if not os.path.exists("entries"):
    os.makedirs("entries")
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({}, f)


def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

def detect_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    text_lower = text.lower()

    sad_keywords = ["sad", "depress", "cry", "unhappy", "down", "lonely", "hopeless", "tired", "exhausted", "miserable",
                    "hurt", "broken", "helpless", "worthless", "upset", "pain", "sorrow", "grief", "heartbroken",
                    "gloomy", "disappointed", "overwhelmed"]

    happy_keywords = ["happy", "joy", "excited", "love", "great", "amazing", "wonderful", "fantastic", "cheerful",
                      "delighted", "content", "smile", "laugh", "fun", "blessed", "grateful", "proud", "peaceful",
                      "optimistic", "good", "satisfied", "hurrah", "yay"]

    neutral_keywords = ["okay", "fine", "normal", "average", "nothing", "alright", "so-so", "neutral", "meh"]

    # keyword fallback
    if any(word in text_lower for word in sad_keywords):
        return "Sad", 100
    if any(word in text_lower for word in happy_keywords):
        return "Happy", 100
    if any(word in text_lower for word in neutral_keywords):
        return "Neutral", 100

    # fallback to polarity thresholds
    if polarity > 0.2:
        return "Happy", round(polarity * 100, 2)
    elif polarity < -0.05:
        return "Sad", round(abs(polarity) * 100, 2)
    else:
        return "Neutral", round(abs(polarity) * 100, 2)

@app.route("/")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/save", methods=["POST"])
@app.route("/save", methods=["POST"])
def save_entry():
    if "username" not in session:
        return jsonify({"message": "Please log in first."}), 401

    data = request.get_json()
    entry_text = data.get("entry", "")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    emotion, confidence = detect_emotion(entry_text)

    entry_data = {
        "text": entry_text,
        "timestamp": timestamp,
        "hash": generate_hash(entry_text + timestamp),
        "emotion": emotion,
        "confidence": confidence,
        "user": session["username"]
    }

    # Save using username in the filename to separate users cleanly
    filename = f"entries/{timestamp.replace(':', '-')}_{session['username']}.json"
    with open(filename, "w") as f:
        json.dump(entry_data, f, indent=4)

    return jsonify({
        "message": "Entry saved successfully!",
        "hash": entry_data["hash"],
        "emotion": emotion,
        "confidence": confidence
    })


@app.route("/entries")
@app.route("/entries")
def view_entries():
    if "username" not in session:
        return redirect(url_for("login"))

    entries = []
    emotion_counts = {"Happy": 0, "Sad": 0, "Neutral": 0}
    
    for file in os.listdir("entries"):
        if file.endswith(".json"):
            with open(os.path.join("entries", file), "r") as f:
                data = json.load(f)
                # Only include entries of the logged-in user
                if data.get("user") == session["username"]:
                    entries.append(data)
                    emotion = data.get("emotion")
                    if emotion in emotion_counts:
                        emotion_counts[emotion] += 1

    entries.sort(key=lambda x: x["timestamp"], reverse=True)
    return render_template("entries.html", entries=entries, emotion_counts=emotion_counts)



# ========== BlockDAG Publish Simulation ========== #
@app.route("/publish/<hash>", methods=["POST"])
def publish_to_blockdag(hash):
    entry_file = None
    for file in os.listdir("entries"):
        if file.endswith(".json"):
            with open(os.path.join("entries", file), "r") as f:
                data = json.load(f)
                if data.get("hash") == hash:
                    entry_file = file
                    timestamp = data.get("timestamp")
                    break
    if not entry_file:
        return jsonify({"message": "Entry not found!"}), 404

    ledger_file = "blockdag_ledger.json"
    if os.path.exists(ledger_file):
        with open(ledger_file, "r") as f:
            ledger = json.load(f)
    else:
        ledger = []

    ledger.append({
        "hash": hash,
        "timestamp": timestamp
    })

    with open(ledger_file, "w") as f:
        json.dump(ledger, f, indent=4)

    return jsonify({"message": "✅ Successfully published to BlockDAG!"}), 200
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("users.json", "r") as f:
            users = json.load(f)

        if username in users:
            return "Username already exists."

        users[username] = generate_hash(password)
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("users.json", "r") as f:
            users = json.load(f)

        if username in users and users[username] == generate_hash(password):
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return "Invalid username or password."
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__== "__main__":
    app.run(debug=True)