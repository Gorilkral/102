import json

def giris():
    isim = input("isminiyaz: ")
    sifre = input ("sifreyazmoruk: ")
    with open("userData.json", "r", encoding='utf-8') as q:
        hesaplar = json.load(q)
        try:
            if isim not in hesaplar:
                raise ValueError("Böyle bir hesap bulunamadı.")
            if sifre == hesaplar[isim]:
               print("giris basarili!")
            else:
                raise ValueError("Kullanıcı adı veya şifre yanlış.")
        except ValueError as e:
            print(e)
            giris()
def kayit():
    isim = input("isim yaz moruk: ")
    sifre = input("sifren ne: ")
    with open("userData.json", "r", encoding='utf-8') as z:
        hesaplar = json.load(z)
        hesaplar[isim] = sifre

        with open("userData.json", "w", encoding='utf-8') as c:
            json.dump(hesaplar, c, indent=4, ensure_ascii=False)
        print("Kayıt başarılı.")

sex = input("kayit mi giris mi usta? ")
if sex == "kayit":
    kayit()
elif sex == "giris":
    giris()
else:
    print("boylebiseyyokorospucocugu")