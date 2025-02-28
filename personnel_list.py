import tkinter as tk
from tkinter import ttk
import pandas as pd
import subprocess

# CSV dosyasını oku
def load_data():
    df = pd.read_csv('personel.csv')  # Dosya yolunun doğru olduğundan emin olun
    return df

# Listeyi oluştur
def create_personel_list():
    # Veriyi al
    df = load_data()

    # Tkinter penceresini oluştur ve boyutları ayarla
    window = tk.Tk()
    window.title("Personel Bilgileri")
    window.geometry("1920x1080")  # Çözünürlük 1920x1080 olarak ayarlanır

    # Treeview tablosunu oluştur (Excel gibi)
    tree = ttk.Treeview(window, columns=("isim","soyisim", "yas", "kurallihlali"), show="headings", height=20)
    
    # Sütun başlıklarını ayarla
    tree.heading("isim", text="İsim")
    tree.heading("soyisim", text="Soy İsim")
    tree.heading("yas", text="Yaş")
    tree.heading("kurallihlali", text="Kural İhlali")
    
    # Sütun genişliklerini ayarla
    tree.column("isim", width=400)
    tree.column("soyisim", width=400)
    tree.column("yas", width=150,anchor="center")
    tree.column("kurallihlali", width=250,anchor="center")

    # Yazı tipini büyüt
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 14))  # Tüm yazı tipini büyütüyoruz
    style.configure("Treeview.Heading", font=("Arial", 16))  # Başlık yazı tipini büyütüyoruz

    # Verileri tabloya ekle
    for index, row in df.iterrows():
        tree.insert("", tk.END, values=(row["isim"],row["soyisim"], row["yas"], row["kurallihlali"]))

    # Treeview'i ekranın sağ tarafına yerleştir
    tree.grid(row=0, column=1, padx=20, pady=20)

    # Geri butonu
    def go_back():
        window.destroy()
        subprocess.run(["python", "main_menu.py"])
    

    back_button = tk.Button(window, text="Geri", command=go_back, font=("Arial", 16), width=10, height=2)
    back_button.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

    window.mainloop()

# Ana fonksiyon
if __name__ == "__main__":
    create_personel_list()
