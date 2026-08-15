# AI Blockchain Mood Journal

A private mood journal backed by AI emotion detection and blockchain integrity.

Live demo: https://ai-blockchain-mood-journal.onrender.com (hosted on Render's free tier; may take 20–30 seconds to wake up on first load)

Built solo by Gagandeep for the BlockDAG Hackathon 2025.

## Overview

This project combines AI and Web3 to build a private, tamper-evident mood journal. Users write daily journal entries through a web interface; an AI model detects the underlying emotion, and each entry is hashed and recorded on the BlockDAG blockchain, proving that an entry existed at a given time without exposing its content.

## Objective

To create a space where users can log their feelings freely while addressing two concerns common in typical journaling apps:

- Emotional well-being tracking — surfacing mood patterns over time
- Data privacy and proof of authenticity — using cryptographic hashing and blockchain timestamps, so entries can be verified without being exposed

## How It Works

1. Write — the user writes a journal entry through the web interface
2. AI detection — TextBlob analyzes the entry and classifies it as Happy, Sad, or Neutral
3. Hashing — the entry is hashed using SHA-256 to secure its content and detect tampering
4. Blockchain record — the hash and timestamp are published to the BlockDAG blockchain, establishing proof of existence without revealing the entry's content
5. History view — users can review past entries and see their emotional trend over time

## Features

- Private journal entries with individual login/register accounts
- AI-based mood detection on every entry
- SHA-256 hashing of entry content for tamper detection
- BlockDAG publish flow, built and demonstrated for the hackathon
- Emotion trend visualization over time
- Per-user data segregation

## My Contribution

Built independently, end-to-end, for the BlockDAG Hackathon 2025:

- Designed and implemented the full Flask backend and web interface
- Integrated TextBlob for emotion classification on journal text
- Implemented SHA-256 hashing for entry integrity
- Built the BlockDAG publishing flow to timestamp and record entry hashes
- Designed the trend visualization for historical mood data
- Deployed and hosted the live demo on Render

## Tech Stack

Frontend: HTML, CSS, JavaScript, Chart.js
Backend: Python, Flask, TextBlob
Web3 layer: BlockDAG blockchain (hash + timestamp)
Storage: JSON-based entry storage
Deployment: Render

## Running Locally

```bash
git clone https://github.com/Gagan2435/AI-Blockchain-Mood-Journal.git
cd AI-Blockchain-Mood-Journal

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

pip install -r requirements.txt
python app.py
```

Then visit `http://127.0.0.1:5000`.

## Future Plans

- Move to more advanced emotion detection using HuggingFace models or a custom-trained emotion classifier
- Use IPFS for encrypted, decentralized entry storage
- Move from the current publish flow to a real smart contract deployment on the BlockDAG blockchain
- Build a deeper analytics dashboard for long-term emotional trend analysis
- Open the project up for community contributions

## License

MIT
