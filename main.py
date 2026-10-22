import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        weight = float(weight_entry.get().replace(",", "."))
        height = float(height_entry.get().replace(",", "."))

        if weight <= 0 or height <= 0:
            messagebox.showerror("Hata", "Boy ve kilo sıfırdan büyük olmalı!")
            return

        # Boy santimetre olarak girilir
        boy_metre = height / 100
        bmi = weight / (boy_metre ** 2)

        if bmi < 18.5:
            kategori = "Zayıf"
        elif bmi < 25:
            kategori = "Normal"
        elif bmi < 30:
            kategori = "Fazla kilolu"
        else:
            kategori = "Obezite aralığı"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nKategori: {kategori}"
        )

    except ValueError:
        messagebox.showerror(
            "Hata",
            "Lütfen geçerli bir boy ve kilo girin!"
        )


# Ana pencere
pencere = tk.Tk()
pencere.title("BMI Calculator")
pencere.geometry("350x350")
pencere.resizable(False, False)
pencere.configure(bg="#eaf2f8")

# Başlık
title = tk.Label(
    pencere,
    text="BMI Calculator",
    font=("Arial", 20, "bold"),
    bg="#eaf2f8",
    fg="#2c3e50"
)
title.pack(pady=20)

# Kilo alanı
tk.Label(
    pencere,
    text="Kilonuz (kg):",
    font=("Arial", 12),
    bg="#eaf2f8"
).pack()

weight_entry = tk.Entry(pencere, font=("Arial", 12), justify="center")
weight_entry.pack(pady=5)

# Boy alanı
tk.Label(
    pencere,
    text="Boyunuz (cm):",
    font=("Arial", 12),
    bg="#eaf2f8"
).pack()

height_entry = tk.Entry(pencere, font=("Arial", 12), justify="center")
height_entry.pack(pady=5)

calculate_button = tk.Button(
    pencere,
    text="BMI Hesapla",
    font=("Arial", 12, "bold"),
    bg="#3498db",
    fg="white",
    command=calculate
)
calculate_button.pack(pady=15)

# Sonuç alanı
result_label = tk.Label(
    pencere,
    text="Sonuç burada gösterilecek",
    font=("Arial", 12, "bold"),
    bg="#eaf2f8",
    fg="#2c3e50"
)
result_label.pack(pady=5)

pencere.mainloop()
