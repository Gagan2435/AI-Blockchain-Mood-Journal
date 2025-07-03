from flask import Flask, render_template, request, jsonify
from datetime import datetime
import hashlib
import json
import os

app = Flask(__name__)

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
    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    entry_data = {
        "text": entry_text,
        "timestamp": timestamp,
        "hash": generate_hash(entry_text + timestamp)
    }

    filename = f"entries/{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(entry_data, f, indent=4)

    return jsonify({"message": "Entry saved successfully!", "hash": entry_data["hash"]})

if __name__ == "__main__":
    app.run(debug=True)
