<p align="center">
  <img src="screenshots/logo.png" width="250">
</p>

🚨 AI-SOC-AutoResponse
Autonomous SOC Engine for Alert Triage, Threat Classification & Automated Response

AI-SOC-AutoResponse is an intelligent lightweight SOAR engine designed to assist SOC teams by automating alert analysis, threat scoring, IOC enrichment, and response recommendation.
Built for speed, clarity, and real-world SOC workflows.

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Framework](https://img.shields.io/badge/Framework-Flask-orange)
![AI](https://img.shields.io/badge/AI-NLP%20Engine-purple)
![Security](https://img.shields.io/badge/SOC-Automation-red)

---

⚡ Features
AI-Driven Alert Classification
Uses NLP + rule-based logic to classify logs: malware, phishing, brute-force, beaconing, suspicious access, and more.

---

Real-time IOC Enrichment
Fetches WHOIS, domain age, DNS records, and reputation indicators.

Risk Scoring Engine
Produces a final severity score (Low/Medium/High/Critical) based on indicators.

Auto-Response Suggestions
Suggests actions such as block, isolate endpoint, disable user, reset password, revoke token, or escalate to Tier-2.

Clean JSON API
Integrates with SIEM, SOAR, ELK pipelines, or scripts.

Simple Flask Dashboard
Submit logs, view analysis instantly, clean UI for demonstrations and SOC assessments.

---

🧠 How It Works
Input: Raw alert/log from SIEM, firewall, endpoint, or proxy
AI Engine: NLP classifier + custom rule evaluator
Correlation: Extracts IPs, domains, usernames, event types
Enrichment: Domain reputation, IP info, age, keywords, anomalies
Risk Score: Weighted system to calculate overall severity
Response Suggestion: Smart decision engine

Output: JSON + dashboard visualization

---

🚀 Run Locally
git clone https://github.com/blacklatch-cybersecurity/ai-soc-autoresponse.git
cd ai-soc-autoresponse
pip install -r requirements.txt
./run.sh

---

Dashboard runs on:
http://127.0.0.1:9600

🧪 API Example
Request
POST /api/analyze
Content-Type: application/json

{
  "log": "Failed SSH login from 185.22.13.9 user root"
}

Response
{
  "intent": "Brute Force",
  "risk": "High",
  "severity_score": 85,
  "recommended_action": "Block IP + enable rate limiting",
  "iocs": ["185.22.13.9"]
}

---

📂 Project Structure
ai-soc-autoresponse/
│── app/
│   ├── app.py            # Dashboard + API
│   ├── templates/        # UI
│   └── static/           # CSS/JS
│
│── engine/
│   ├── classify.py       # Log classifier
│   ├── enrich.py         # IOC enrichment
│   ├── scorer.py         # Severity scoring
│   └── response.py       # Playbook actions
│
│── data/
│── run.sh
│── requirements.txt
│── README.md

---

🛡️ Future Enhancements
Integrate MITRE ATT&CK mapping
Add auto-block API for firewall + EDR
Add threat graph visualization
Add webhook notifications (Slack, Teams, Telegram)
Add live streaming log analyzer

---

👑 Author
Built by Blacklatch Cybersecurity Defense — Autonomous Threat Engineering & Cyber Deception Systems.
