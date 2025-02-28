import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime
import subprocess

def geri_butonu():
    # Geri butonuna basıldığında sayfayı kapat
    root.destroy()
    subprocess.run(["python", "main_menu.py"])
    

def raporu_kaydet():
    yazar = yazar_entry.get()
    alici = alici_entry.get()
    tarih = tarih_entry.get()
    icerik = icerik_text.get("1.0", "end-1c")

    if not yazar or not alici or not tarih or not icerik:
        messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
        return
    
    # CSV dosyasına kaydet
    with open("raporlar.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([yazar, alici, tarih, icerik])
    
    messagebox.showinfo("Başarılı", "Rapor başarıyla kaydedildi.")
    
    # Alanları temizle
    yazar_entry.delete(0, tk.END)
    alici_entry.delete(0, tk.END)
    tarih_entry.delete(0, tk.END)
    icerik_text.delete("1.0", tk.END)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Rapor Oluşturma")
root.geometry("1920x1080")  # 1920x1080 çözünürlüğü

# Sayfa elemanlarını ortalamak için frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Yazar
yazar_label = tk.Label(frame, text="Raporu yazan kişi:", font=("Arial", 14))
yazar_label.grid(row=1, column=0, padx=20, pady=10)
yazar_entry = tk.Entry(frame, font=("Arial", 14), width=50)
yazar_entry.grid(row=1, column=1, padx=20, pady=10)

# Alıcı
alici_label = tk.Label(frame, text="Raporun yazıldığı kişi:", font=("Arial", 14))
alici_label.grid(row=2, column=0, padx=20, pady=10)
alici_entry = tk.Entry(frame, font=("Arial", 14), width=50)
alici_entry.grid(row=2, column=1, padx=20, pady=10)

# Tarih
tarih_label = tk.Label(frame, text="Raporun tarihi (gg-aa-yyyy):", font=("Arial", 14))
tarih_label.grid(row=3, column=0, padx=20, pady=10)
tarih_entry = tk.Entry(frame, font=("Arial", 14), width=50)
tarih_entry.grid(row=3, column=1, padx=20, pady=10)
tarih_entry.insert(0, datetime.now().strftime("%d-%m-%Y"))  # Bugünün tarihini varsayılan olarak ekle

# Rapor içeriği
icerik_label = tk.Label(frame, text="Rapor İçeriği:", font=("Arial", 14))
icerik_label.grid(row=4, column=0, padx=20, pady=10)
icerik_text = tk.Text(frame, font=("Arial", 14), width=50, height=8)
icerik_text.grid(row=4, column=1, padx=20, pady=10)

# Kaydet butonu
kaydet_button = tk.Button(frame, text="Raporu Kaydet", font=("Arial", 14), command=raporu_kaydet)
kaydet_button.grid(row=5, column=0, columnspan=2, pady=20)

# Geri butonu
geri_button = tk.Button(root, text="Geri", font=("Arial", 14), command=geri_butonu)
geri_button.place(relx=0.01, rely=0.01, anchor="nw")



# GUI'yi başlat
root.mainloop()
