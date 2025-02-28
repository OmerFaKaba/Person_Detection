import tkinter as tk
from tkinter import messagebox
import subprocess

def open_cameras():
    root.destroy()
    subprocess.run(["python", "yolo.py"])

def open_personnel_list():
    root.destroy()
    subprocess.run(["python", "personnel_list.py"])

def open_records():
    root.destroy()
    subprocess.run(["python", "records.py"])

def open_report():
    root.destroy()
    subprocess.run(["python", "report.py"])

def log_out():
    root.destroy()
    subprocess.run(["python", "login.py"])

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Ana Sayfa")
root.geometry("1920x1080")  # 1920x1080 çözünürlük
root.configure(bg="white")

# Sol taraftaki çizgi
line = tk.Frame(root, width=5, height=1080, bg="black")
line.place(x=960, y=0)  # Ekranın tam ortasında bir çizgi

# Ekranın sol kısmındaki büyük italik yazı (The Vision)
label = tk.Label(root, text="THE VISION", font=("Arial", 80, "italic"), bg="white")
label.place(relx=0.25, rely=0.5, anchor="center")  # Sol tarafta tam ortada

# Butonlar: Sağ üst, sol üst, sağ alt, sol alt
button1 = tk.Button(root, text="Kameralar Ekranı", font=("Arial", 20), command=open_cameras)
button1.place(x=1500, y=100, width=250, height=250)  # Sağ üst buton

button2 = tk.Button(root, text="Personel Listesi", font=("Arial", 20), command=open_personnel_list)
button2.place(x=1100, y=100, width=250, height=250)  # Sol üst buton

button3 = tk.Button(root, text="Kayıtlar", font=("Arial", 20), command=open_records)
button3.place(x=1500, y=450, width=250, height=250)  # Sağ alt buton

button4 = tk.Button(root, text="Rapor Oluştur", font=("Arial", 20), command=open_report)
button4.place(x=1100, y=450, width=250, height=250)  # Sol alt buton

button5 = tk.Button(root, text="Log Out", font=("Arial", 20), command=log_out)
button5.place(x=1100, y=900, width=150, height=50)  

# Pencereyi sürekli açık tut
root.mainloop()
