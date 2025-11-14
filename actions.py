import time

def block_ip(ip):
    print(f"[ACTION] Blocking IP: {ip}")
    time.sleep(1)
    return f"IP {ip} blocked."

def disable_user(user):
    print(f"[ACTION] Disabling user: {user}")
    time.sleep(1)
    return f"User {user} disabled."

def send_webhook(msg):
    print(f"[ACTION] Sending webhook: {msg}")
    return "Webhook delivered."
