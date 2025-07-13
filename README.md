🌱 AI Blockchain Mood Journal
A safe space for your feelings — analyzed by AI, sealed with Web3.

Theme: AI × Smart Contracts (BlockDAG Hackathon 2025)

 🌐 **Live Demo:**

🔗 [https://ai-blockchain-mood-journal.onrender.com](https://ai-blockchain-mood-journal.onrender.com)

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

