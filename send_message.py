import os
import requests

#my data
telegram_token = os.environ.get("TELEGRAM_API_KEY")
chat_id = "5586625183"



def send_message(txt, date):
    msg = date + "\n" + txt
    url = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + msg
    url = url.replace("#", "%23")
    response = requests.get(url)
    return response.json()
