from kurs import kurs_ol, hisobla_kurs
from bot import send_message
from keyboard import get_reply_keyboard

def handler_message(text, chat_id):
    if text.lower() == '/start':
        send_message(chat_id, "Valyutani tanlang yoki misol uchun USD 100 deb yozing:", reply_markup=get_reply_keyboard())

    elif text.upper() in ['USD', 'EUR', 'RUB', 'UZS']:
        kurs = kurs_ol(text.upper())
        if kurs:
            send_message(chat_id, f"1 {text.upper()} ≈ {kurs} so'm")
        else:
            send_message(chat_id, "Valyuta topilmadi.")

    elif len(text.split()) == 2:
        valyuta, summa = text.upper().split()
        try:
            summa = float(summa)
            natija = hisobla_kurs(valyuta, summa)
            send_message(chat_id, natija)
        except ValueError:
            send_message(chat_id, "Iltimos, summani to'g'ri yozing. Masalan: USD 100")
    else:
        send_message(chat_id, "Bunday valyuta topilmadi. Masalan: USD, EUR, RUB deb yozing.")
