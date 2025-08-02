import requests
from config import URL
from settings import TOKEN

def get_updates(offset =None):
    params = {
        'timeout' : 100,
        'offset' : offset
    }
    responce = requests.get(URL + 'getUPdates', params=params)
    return responce.json()

URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'



def send_message(chat_id, text, reply_markup=None):
    data = {
        'chat_id': chat_id,
        'text': text
    }

    if reply_markup:
        data['reply_markup'] = reply_markup

    response = requests.post(URL, json=data)
    print(response.json())