from bot import send_message
from kurs import kurs_ol

def handle_currency(chat_id, valyuta):
    javob = kurs_ol(valyuta)
    send_message(chat_id, javob)
