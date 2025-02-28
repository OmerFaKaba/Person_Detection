import subprocess

import pandas as pd
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar

# CSV dosyasını oku (Türkçe karakter desteği)
csv_dosyasi = "raporlar.csv"  # CSV dosyanızın adı
df = pd.read_csv(csv_dosyasi, encoding="utf-8")  # Alternatif olarak encoding="latin1" deneyebilirsiniz

# Tarih formatını düzelt (varsayılan format DD-MM-YYYY ise)
df['tarih'] = pd.to_datetime(df['tarih'], format="%d-%m-%Y").dt.strftime("%Y-%m-%d")

# Ana pencere
root = Tk()
root.title("Rapor Görüntüleyici")
root.geometry("1920x1080")

# Sol üstteki geri butonu
def geri_don():
    rapor_liste.selection_clear(0, END)
    takvim.selection_clear()
    root.destroy()
    subprocess.run(["python", "main_menu.py"])

geri_button = Button(root, text="Geri", command=geri_don)
geri_button.place(x=10, y=10)

# Sol taraf: Takvim
takvim_frame = Frame(root)
takvim_frame.place(x=0, y=50, width=960, height=1030)

takvim = Calendar(takvim_frame, selectmode="day", date_pattern="yyyy-mm-dd")
takvim.pack(expand=True, fill="both")

# Sağ taraf: Liste
liste_frame = Frame(root)
liste_frame.place(x=960, y=0, width=960, height=1080)

# Liste kutusu
rapor_liste = Listbox(liste_frame, font=("Arial", 14))
rapor_liste.pack(expand=True, fill="both")

# Raporları listele
for index, row in df.iterrows():
    rapor_liste.insert(END, f"{row['yazan']} -> {row['kime']} | {row['tarih']} | {row['rapor']}")

# Liste tıklama işlevi
def rapor_sec(event):
    secili = rapor_liste.curselection()
    if secili:
        index = secili[0]
        tarih = df.iloc[index]['tarih']
        takvim.selection_set(tarih)

rapor_liste.bind("<<ListboxSelect>>", rapor_sec)

root.mainloop()
