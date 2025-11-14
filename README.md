# 🚨 AI-SOC-AutoResponse  
### Autonomous SOC Engine for Alert Triage, Threat Classification & Automated Response

AI-SOC-AutoResponse is an intelligent lightweight SOAR engine built to automate alert triage, IOC enrichment, threat scoring, and response recommendations.  
Ideal for SOC teams that need clarity, speed, and smart analysis.

---

## 📊 **Status**
**Language:** Python  
**Framework:** Flask  
**Category:** AI Security / SOC Automation  

---

## ⚡ **Features**

### 🔹 **AI-Driven Alert Classification**  
Uses NLP + rules to classify logs into:  
- Malware  
- Phishing  
- Brute-force  
- Beaconing  
- Privilege misuse  
- Suspicious access

### 🔹 **Real-Time IOC Enrichment**  
Automatic lookup of:  
- WHOIS  
- Domain age  
- DNS (A, NS, MX)  
- Reputation signals  

### 🔹 **Risk Scoring Engine**  
Weighted scoring → **Low / Medium / High / Critical**.

### 🔹 **Auto-Response Suggestions**  
Recommends actions like:  
- Block IP  
- Isolate endpoint  
- Disable user  
- Reset password  
- Escalate to Tier-2  

### 🔹 **Clean JSON API**  
Works with SIEM, SOAR, ELK, custom pipelines.

### 🔹 **Simple Flask Dashboard**  
Enter logs → View instant AI analysis.

---

## 🧠 **How It Works**

1. **Input:** Raw log / alert  
2. **AI Classifier:** NLP + keyword logic  
3. **IOC Extraction:** IPs, domains, usernames  
4. **Enrichment:** WHOIS + DNS + reputation  
5. **Risk Score:** Weighted scoring engine  
6. **Response Suggestion:** Dynamic SOC playbooks  
7. **Output:** JSON + Dashboard view  

---

## 🚀 **Run Locally**

```bash
git clone https://github.com/blacklatch-cybersecurity/ai-soc-autoresponse.git
cd ai-soc-autoresponse
pip install -r requirements.txt
./run.sh

Dashboard:
http://127.0.0.1:9600

---

🧪 API Example
Request

POST /api/analyze

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
│   ├── app.py           # Dashboard + API
│   ├── templates/       # UI
│   └── static/          # CSS/JS
│
│── engine/
│   ├── classify.py      # NLP classifier
│   ├── enrich.py        # IOC lookups
│   ├── scorer.py        # Severity engine
│   └── response.py      # Response playbooks
│
│── data/
│── run.sh
│── requirements.txt
│── README.md

🛡️ Future Enhancements
MITRE ATT&CK mapping
Auto-block APIs (Firewall / EDR)
Threat graph visualization
Slack / Teams / Telegram webhooks
Live log streaming

👑 Author
Blacklatch Cybersecurity Defense
Autonomous Threat Engineering & Cyber Deception Systems
