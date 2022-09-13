import os
import requests

telegram_token = os.environ.get("TELEGRAM_API_KEY")

def delete_messages(message_id, chat_id):
    url = 'https://api.telegram.org/bot' + telegram_token + '/deleteMessage?chat_id=' + chat_id + '&message_id=' + message_id + '&parse_mode=Markdown&text='
    response = requests.get(url)
    return response.json()
