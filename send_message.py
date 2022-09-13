import os
import requests
import json

telegram_token = os.environ.get("TELEGRAM_API_KEY")


def send_message(txt, date, chat_id):
    #return to this msg after testing
    #msg = date + "\n" + txt
    msg = txt
    url = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg
    url = url.replace("#", "%23")

    #response with message data
    response = requests.get(url).json()
    msg_id = str(response['result']['message_id'])           
    return response, msg_id
