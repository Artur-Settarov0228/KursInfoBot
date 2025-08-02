
import requests

responce = requests.get('https://cbu.uz/oz/arkhiv-kursov-valyut/json/')
data = responce.json()



def kurs_ol(valyuta):
        try:
             for item in data:
                if item in data:
                   return f"1 {item['Ccy']} = {item['Rate']} som ({item['CcNm_UZ']})"
             return "Bunday valyuta topilmadi. Masalan: USD, UZS, EUR"
        except:
             " ERROR!. Kursni olishda xatolik yuz berdi."
   

        