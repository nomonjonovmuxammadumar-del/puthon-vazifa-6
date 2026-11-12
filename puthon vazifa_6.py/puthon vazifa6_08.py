
import requests
 
URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
 
 
def son_formatla(son):
    return f"{son:.2f}".rstrip("0").rstrip(".")
 
 
def kurslarni_ol():
    javob = requests.get(URL, timeout=10)
    javob.raise_for_status()
    return javob.json()
 
 
def valyuta_top(kurslar, kod):
    for valyuta in kurslar:
        if valyuta["Ccy"] == kod:
            return valyuta
    return None
 
 
def main():
    kod = input("Valyuta kodini kiriting: ").strip().upper()
    miqdor_matn = input("Miqdorni kiriting: ").strip().replace(",", ".")
 
    if len(kod) != 3 or not kod.isalpha():
        print("Xato: valyuta kodi 3 ta harfdan iborat bo'lishi kerak (masalan, USD).")
        return
 
    try:
        miqdor = float(miqdor_matn)
    except ValueError:
        print("Xato: miqdor son bo'lishi kerak.")
        return
 
    if miqdor <= 0:
        print("Xato: miqdor 0 dan katta bo'lishi kerak.")
        return
 
    try:
        kurslar = kurslarni_ol()
    except (requests.RequestException, ValueError):
        print("Xato: kurslarni olib bo'lmadi. Internetni tekshiring.")
        return
 
    valyuta = valyuta_top(kurslar, kod)
    if valyuta is None:
        print("Xato: bunday valyuta kodi topilmadi.")
        return
 
    nominal = float(valyuta["Nominal"])
    kurs = float(valyuta["Rate"]) / nominal
    jami = miqdor * kurs
 
    print()
    print("Valyuta:", valyuta["CcyNm_UZ"])
    print(f"Miqdor: {son_formatla(miqdor)} {kod}")
    print(f"1 {kod} kursi: {son_formatla(kurs)} so'm")
    print()
    print(f"Jami: {son_formatla(jami)} so'm")
 
 
if __name__ == "__main__":
    main()
 