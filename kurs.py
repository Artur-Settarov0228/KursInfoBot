
import requests


def kurs_ol(valyuta):
    print(f"Valyuta kelib tushdi: {valyuta}")  # DEBUG

    url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'  # Markaziy Bank API
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Valyuta ma'lumotlarini olishda xatolik."

    data = response.json()

    for item in data:
        if item['Ccy'].lower() == valyuta.lower():
            return f"💰 1 {item['Ccy']} = {item['Rate']} so'm"

    return "Bunday valyuta topilmadi. Masalan: USD, EUR, RUB deb yozing."

        