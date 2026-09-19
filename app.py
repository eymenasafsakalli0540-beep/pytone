"""
Mini Projeler Menüsü - API gerektirmez, sadece Python standart kütüphanesi.
Çalıştırmak için:  python mini_projeler.py
"""
import random
import string


def sayi_al(mesaj):
    """Geçerli bir sayı girilene kadar sorar."""
    while True:
        try:
            return float(input(mesaj).replace(",", "."))
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")


# 1) Hesap Makinesi
def hesap_makinesi():
    print("\n--- Hesap Makinesi ---")
    a = sayi_al("Birinci sayı: ")
    islem = input("İşlem (+ - * / ** %): ").strip()
    b = sayi_al("İkinci sayı: ")
    try:
        sonuc = {
            "+": a + b, "-": a - b, "*": a * b,
            "/": a / b if b != 0 else None,
            "**": a ** b,
            "%": a % b if b != 0 else None,
        }[islem]
        print("Hata: Sıfıra bölme!" if sonuc is None else f"Sonuç: {sonuc}")
    except KeyError:
        print("Geçersiz işlem.")


# 3) Zar Atma
def zar_at():
    print("\n--- Zar Atma ---")
    adet = int(sayi_al("Kaç zar atılsın? "))
    zarlar = [random.randint(1, 6) for _ in range(max(adet, 1))]
    print("Zarlar:", zarlar, "| Toplam:", sum(zarlar))


# 5) Sayı Tahmin Oyunu
def tahmin_oyunu():
    print("\n--- Sayı Tahmin Oyunu ---")
    gizli = random.randint(1, 100)
    hak = 0
    print("1 ile 100 arasında bir sayı tuttum.")
    while True:
        tahmin = int(sayi_al("Tahminin: "))
        hak += 1
        if tahmin < gizli:
            print("Daha büyük!")
        elif tahmin > gizli:
            print("Daha küçük!")
        else:
            print(f"Bildin! {hak} denemede buldun.")
            break


# 7) Bahşiş Hesaplayıcı
def bahsis():
    print("\n--- Bahşiş Hesaplayıcı ---")
    hesap = sayi_al("Hesap tutarı: ")
    oran = sayi_al("Bahşiş yüzdesi: ")
    kisi = max(int(sayi_al("Kaç kişi? ")), 1)
    bahsis_tutari = hesap * oran / 100
    toplam = hesap + bahsis_tutari
    print(f"Bahşiş: {bahsis_tutari:.2f} | Toplam: {toplam:.2f} | Kişi başı: {toplam / kisi:.2f}")


# 10) Taş Kağıt Makas
def tas_kagit_makas():
    print("\n--- Taş Kağıt Makas ---")
    secenekler = ["tas", "kagit", "makas"]
    yenen = {"tas": "makas", "kagit": "tas", "makas": "kagit"}
    while True:
        oyuncu = input("Seçimin (tas/kagit/makas, çıkış için q): ").strip().lower()
        if oyuncu == "q":
            break
        if oyuncu not in secenekler:
            print("Geçersiz seçim.")
            continue
        bilgisayar = random.choice(secenekler)
        print("Bilgisayar:", bilgisayar)
        if oyuncu == bilgisayar:
            print("Berabere!")
        elif yenen[oyuncu] == bilgisayar:
            print("Kazandın!")
        else:
            print("Kaybettin!")


# 12) VKİ (BMI) Hesaplayıcı
def bmi():
    print("\n--- VKİ Hesaplayıcı ---")
    boy = sayi_al("Boy (cm): ") / 100
    kilo = sayi_al("Kilo (kg): ")
    if boy <= 0:
        print("Boy sıfırdan büyük olmalı.")
        return
    vki = kilo / boy ** 2
    if vki < 18.5:
        durum = "Zayıf"
    elif vki < 25:
        durum = "Normal"
    elif vki < 30:
        durum = "Fazla kilolu"
    else:
        durum = "Obez"
    print(f"VKİ: {vki:.1f} -> {durum}")


# 13) Şifre Üretici
def sifre_uret():
    print("\n--- Şifre Üretici ---")
    uzunluk = max(int(sayi_al("Şifre uzunluğu: ")), 4)
    havuz = string.ascii_letters + string.digits + "!@#$%&*?"
    # Her türden en az bir karakter garantile
    sifre = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%&*?"),
    ]
    sifre += [random.choice(havuz) for _ in range(uzunluk - 4)]
    random.shuffle(sifre)
    print("Şifren:", "".join(sifre))


# 14) Adam Asmaca
def adam_asmaca():
    print("\n--- Adam Asmaca ---")
    kelimeler = ["python", "program", "bilgisayar", "klavye", "algoritma", "degisken", "fonksiyon"]
    kelime = random.choice(kelimeler)
    bulunan = set()
    hak = 6
    while hak > 0:
        gosterim = " ".join(h if h in bulunan else "_" for h in kelime)
        print(f"\n{gosterim}   (Kalan hak: {hak})")
        if all(h in bulunan for h in kelime):
            print("Tebrikler, kazandın!")
            return
        harf = input("Harf: ").strip().lower()
        if len(harf) != 1 or not harf.isalpha():
            print("Tek bir harf gir.")
        elif harf in bulunan:
            print("Bu harfi zaten denedin.")
        elif harf in kelime:
            bulunan.add(harf)
        else:
            bulunan.add(harf)
            hak -= 1
            print("Yanlış!")
    print(f"Kaybettin! Kelime: {kelime}")


# 20) E-posta Ayırıcı
def eposta_ayir():
    print("\n--- E-posta Ayırıcı ---")
    eposta = input("E-posta adresi: ").strip()
    if eposta.count("@") != 1:
        print("Geçersiz e-posta.")
        return
    kullanici, alan = eposta.split("@")
    print("Kullanıcı adı:", kullanici)
    print("Alan adı:", alan)


MENU = {
    "1": ("Hesap Makinesi", hesap_makinesi),
    "2": ("Zar Atma", zar_at),
    "3": ("Sayı Tahmin Oyunu", tahmin_oyunu),
    "4": ("Bahşiş Hesaplayıcı", bahsis),
    "5": ("Taş Kağıt Makas", tas_kagit_makas),
    "6": ("VKİ Hesaplayıcı", bmi),
    "7": ("Şifre Üretici", sifre_uret),
    "8": ("Adam Asmaca", adam_asmaca),
    "9": ("E-posta Ayırıcı", eposta_ayir),
}


def main():
    while True:
        print("\n===== MİNİ PROJELER =====")
        for anahtar, (ad, _) in MENU.items():
            print(f"{anahtar}) {ad}")
        print("0) Çıkış")
        secim = input("Seçimin: ").strip()
        if secim == "0":
            print("Görüşürüz!")
            break
        if secim in MENU:
            MENU[secim][1]()
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
