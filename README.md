🌱 AI Blockchain Mood Journal
A safe space for your feelings — analyzed by AI, sealed with Web3.

Theme: AI × Smart Contracts (BlockDAG Hackathon 2025)

 🌐 **Live Demo:**

🔗 [https://ai-blockchain-mood-journal.onrender.com](https://ai-blockchain-mood-journal.onrender.com)<div align="center">

# AI Blockchain Mood Journal

### A Private Mood Journal Backed by AI Emotion Detection and Blockchain Integrity

<img src="https://img.shields.io/badge/Hackathon-BlockDAG%202025-1f6feb?style=flat-square" />
<img src="https://img.shields.io/badge/Stack-Flask%20%7C%20TextBlob%20%7C%20BlockDAG-1f6feb?style=flat-square" />
<img src="https://img.shields.io/badge/Status-Working%20Demo-1f6feb?style=flat-square" />

**[Live Demo](https://ai-blockchain-mood-journal.onrender.com)** — hosted on Render's free tier; may take 20–30 seconds to wake up on first load.

</div>

<br>

## Overview

This project combines AI and Web3 to build a private, tamper-evident mood journal. Users write daily journal entries through a simple web interface; an AI model detects the underlying emotion, and each entry is hashed and recorded on the BlockDAG blockchain — proving that an entry existed at a given time, without exposing its content.

Built solo for the **BlockDAG Hackathon 2025**.

<br>

## Objective

To create a space where users can log their feelings freely while addressing two concerns that plague typical journaling apps:

- **Emotional well-being tracking** — surfacing mood patterns over time
- **Data privacy and proof of authenticity** — using cryptographic hashing and blockchain timestamps, so entries can be verified without being exposed

<br>

## How It Works

1. **Write** — the user writes a journal entry through the web interface
2. **AI Detection** — TextBlob analyzes the entry and classifies it as Happy, Sad, or Neutral
3. **Hashing** — the entry is hashed using SHA-256 to secure its content and detect tampering
4. **Blockchain Record** — the hash and timestamp are published to the BlockDAG blockchain, establishing proof of existence without revealing the entry's content
5. **History View** — users can review past entries and see their emotional trend over time

<br>

## Features

- Private journal entries with individual login/register accounts
- AI-based mood detection on every entry
- SHA-256 hashing of entry content for tamper detection
- BlockDAG publish flow, built and demonstrated for the hackathon
- Emotion trend visualization over time
- Per-user data segregation

<br>

## My Contribution

Built independently, end-to-end, for the BlockDAG Hackathon 2025:

- Designed and implemented the full Flask backend and web interface
- Integrated TextBlob for emotion classification on journal text
- Implemented SHA-256 hashing for entry integrity
- Built the BlockDAG publishing flow to timestamp and record entry hashes
- Designed the trend visualization for historical mood data
- Deployed and hosted the live demo on Render

<br>

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Backend | Python, Flask, TextBlob |
| Web3 Layer | BlockDAG blockchain (hash + timestamp) |
| Storage | JSON-based entry storage |
| Deployment | Render |

<br>

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

<br>

## Future Plans

- Move to more advanced emotion detection using HuggingFace models or a custom-trained emotion classifier
- Use IPFS for encrypted, decentralized entry storage
- Move from the current publish flow to a real smart contract deployment on the BlockDAG blockchain
- Build a deeper analytics dashboard for long-term emotional trend analysis
- Open the project up for community contributions

<br>

## License

MIT

<br>

<div align="center">
<sub>Built solo by Gagandeep for the BlockDAG Hackathon 2025</sub>
</div>
(⚠️ May take 20–30 sec to wake up on free Render plan)

🎯 Objective
Create a private, secure mood journal where users can express feelings freely.
Combine AI (emotion detection) + Blockchain (tamper-proof hashes) for:

✅ Emotional well-being tracking
✅ Data privacy
✅ Proof of authenticity using Web3

🛠️ How It Works
✨ Write: Users write a daily journal entry via a clean web interface.

🧠 AI Detection: TextBlob detects the emotion (Happy, Sad, Neutral).

🔒 Hashing: Each entry is hashed (SHA-256) to secure content integrity.

⛓️ Blockchain Storage: Hash + timestamp are stored on the BlockDAG blockchain, proving the entry’s existence without revealing its content.

📊 View History: Users can see past emotional trends .

🌟 Features
✅ Write your feelings privately
✅ AI-powered mood detection
✅ Tamper-proof hashing of entries
✅ BlockDAG publish simulation for hackathon demo
✅ Emotion trends visualization
✅ Simple login/register for personal data segregation

🖼️ Screenshots
✏️ Write Entry	📊 Entries + Graph

💡 Applications
🌿 Personal Mental Health Tracker: Reflect on mood changes.
🔐 Proof of Authenticity: Immutable mood entries on blockchain.
📔 Digital Diary (Web3): For users valuing privacy + emotional awareness.

🚀 Run Locally
git clone https://github.com/Gagan2435/ai-blockchain-mood-journal.git
cd ai-blockchain-mood-journal

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

python app.py
# Visit http://127.0.0.1:5000

🗂️ Tech Stack
Frontend: HTML, CSS, JavaScript, Chart.js

Backend: Python Flask, TextBlob

Web3 Layer: BlockDAG blockchain (hash + timestamp)

Storage: JSON-based entry storage

Deployment: Render (free tier)

🚧 Future Plans (Post Hackathon)
✅ Add advanced emotion detection (using HuggingFace or custom emotion datasets)
✅ Use IPFS for encrypted entry storage
✅ Real smart contract deployment on BlockDAG blockchain
✅ User dashboard with deep emotion trend analysis
✅ Community collaborations + open-source growth

🙌 Acknowledgements
Built solo by Gagandeep for the BlockDAG Hackathon 2025.

📜 License
MIT

