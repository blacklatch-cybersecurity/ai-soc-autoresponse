from flask import Flask, request, render_template, jsonify
from rules_engine import classify_alert
from actions import block_ip, disable_user, send_webhook

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json
    alert = data.get("alert", "")
    severity = classify_alert(alert)

    actions_taken = []

    if severity == "High":
        if "ip" in data:
            actions_taken.append(block_ip(data["ip"]))
        send_webhook("High severity alert!")
    elif severity == "Medium":
        send_webhook("Medium severity event detected.")
    else:
        pass

    return jsonify({
        "alert": alert,
        "severity": severity,
        "actions": actions_taken
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9300)
