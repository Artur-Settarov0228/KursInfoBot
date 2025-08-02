import requests

def kurs_ol(valyuta: str) -> float:
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    data = response.json()

    for val in data:
        if val['Ccy'] == valyuta.upper():
            return float(val['Rate'])
    return None

def hisobla_kurs(valyuta: str, summa: float) -> str:
    kurs = kurs_ol(valyuta)
    if kurs is None:
        return "Bunday valyuta topilmadi. Masalan: USD, EUR, RUB deb yozing."
    natija = summa * kurs
    return f"{summa} {valyuta.upper()} ≈ {natija:.2f} so'm"
