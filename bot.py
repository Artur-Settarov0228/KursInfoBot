import requests
from config import URL

def get_updates(offset =None):
    params = {
        'timeout' : 100,
        'offset' : offset
    }
    responce = requests.get(URL + 'getUPdates', params=params)
    return responce.json()

def send_message(chat_id, text):
    params = {
        'chat_id' : chat_id,
        'text' : text
    }
    requests.get(URL + 'sendMessage', params=params)

