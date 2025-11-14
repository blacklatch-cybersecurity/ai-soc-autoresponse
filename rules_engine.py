import json

def classify_alert(alert):
    txt = alert.lower()

    if "failed login" in txt or "bruteforce" in txt:
        return "High"

    if "suspicious" in txt or "unknown" in txt:
        return "Medium"

    return "Low"
