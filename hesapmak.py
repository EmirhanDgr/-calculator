import emirhan


def hesapla(veriler, secim):

    if "1" in secim:
        print("Ortalama", emirhan.ortalama(veriler))
    if "2" in secim:
        print("Kitle Standart Sapması", emirhan.sigma(veriler))
    if "3" in secim:
        print("Örneklem Standart Sapması", emirhan.s(veriler))
    if "4" in secim:
        print("Kitle Varyansı", emirhan.sigmakare(veriler))
    if "5" in secim:
        print("Örneklem Varyansı", emirhan.skare(veriler))
    if "6" in secim:
        print("MOD", emirhan.mod(veriler))
    if "7" in secim:
        print("Medyan", emirhan.medyan(veriler))
    if "8" in secim:
        print("Çeyreklikler", emirhan.çeyreklikler(veriler))
    if "9" in secim:
        print("Çeyrek Sapma", emirhan.çeyreksapma(veriler))
    if "10" in secim:
        print("Standart Hata", emirhan.standart_hata(veriler))


veri_str = input("Verilerinizi girin (virgülle ayırın): ")
veri = list(map(float, veri_str.split(",")))
secim = input(
    "Hangi hesaplamayı yapmak istersiniz? (1: Ortalama, 2: Kitle Standart Sapması, 3: Örneklem Standart Sapması, 4: Kitle Varyansı, 5: Örneklem Varyansı, 6: MOD, 7: Medyan, 8: Çeyreklikler 9: Çeyrek Sapma "
)

hesapla(veri, secim)
