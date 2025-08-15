import tkinter as tk
from tkinter import messagebox
import emirhan


def hesapla():
    try:
        veri_str = entry_veriler.get()
        veriler = list(map(float, veri_str.split(",")))

        secimler = var_secim.get().split(",")

        results = []

        if "1" in secimler:
            results.append("1. Ortalama: " + str(emirhan.ortalama(veriler)))
        if "2" in secimler:
            results.append("2. Kitle Standart Sapması: " + str(emirhan.sigma(veriler)))
        if "3" in secimler:
            results.append("3. Örneklem Standart Sapması: " + str(emirhan.s(veriler)))
        if "4" in secimler:
            results.append("4. Kitle Varyansı: " + str(emirhan.sigmakare(veriler)))
        if "5" in secimler:
            results.append("5. Örneklem Varyansı: " + str(emirhan.skare(veriler)))
        if "6" in secimler:
            results.append("6. MOD: " + str(emirhan.mod(veriler)))
        if "7" in secimler:
            results.append("7. Medyan: " + str(emirhan.medyan(veriler)))
        if "8" in secimler:
            results.append("8. Çeyreklikler: " + str(emirhan.çeyreklikler(veriler)))
        if "9" in secimler:
            results.append("9. Çeyrek Sapma: " + str(emirhan.çeyreksapma(veriler)))

        result_text = "\n".join(results)
        result_label.config(text=result_text)

    except Exception as e:
        messagebox.showerror("Hata", f"Lütfen geçerli bir sayı giriniz.")


root = tk.Tk()
root.title("StatCalc")
root.geometry("500x550+600+180")


entry_label = tk.Label(root, text="Verilerinizi girin (virgülle ayırın):")
entry_label.pack(pady=10)

entry_veriler = tk.Entry(root, width=40)
entry_veriler.pack()


secim_label = tk.Label(
    root,
    text=(
        "Hangi hesaplamayı yapmak istersiniz? \n"
        "Birden fazla hesap yapmak istiyorsanız virgül ile ayırın. \n"
        "1: Ortalama\n"
        "2: Kitle Standart Sapması\n"
        "3: Örneklem Standart Sapması\n"
        "4: Kitle Varyansı\n"
        "5: Örneklem Varyansı\n"
        "6: MOD\n"
        "7: Medyan\n"
        "8: Çeyreklikler\n"
        "9: Çeyrek Sapma"
    ),
)
secim_label.pack(pady=10)

var_secim = tk.Entry(root, width=40)
var_secim.pack()


hesapla_button = tk.Button(root, text="Hesapla", command=hesapla)
hesapla_button.pack(pady=20)


result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()
