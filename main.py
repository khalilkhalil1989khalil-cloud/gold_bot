import os
from flask import Flask, request
import telegram

app = Flask(__name__)

TOKEN = "8788812041:AAEQURVIZXgQ2HxF9W4dQRjG6b1EWMVdkVI"
bot = telegram.Bot(token=TOKEN)

@app.route('/')
def home():
    return "Bot is running 24/7!"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        return "ok"
    return "ok"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
