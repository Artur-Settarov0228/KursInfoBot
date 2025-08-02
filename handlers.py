from kurs import kurs_ol
from bot import send_message


def handler_message(text, chat_id):
    if text.lower() == '/start':
        send_message(chat_id, "Xush kelibsiz! Masalan (USD, UZS va RUB ) deb yozing.") 
    else:
        javob = kurs_ol(text)
        send_message(chat_id, javob)
        




