import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import subprocess

# Kullanıcı adı ve şifre
USERNAME = "admin@gmail.com"
PASSWORD = "123"


# Kullanıcı giriş kontrolü
def login(role):
    username = username_entry.get()
    password = password_entry.get()

    # Önce hata mesajını temizle
    for widget in error_frame.winfo_children():
        widget.destroy()

    # Kullanıcı adı kontrolü
    if not username.endswith("@gmail.com"):
        error_label = tk.Label(error_frame, text="Kullanıcı adı '@gmail.com' ile bitmeli!", font=("Helvetica", 12),
                               fg="red", bg="#f7f7f7")
        error_label.pack()
        return

    if username == USERNAME and password == PASSWORD:

        # İlgili sayfayı çalıştır
        if role == "Admin":
            root.destroy()
            subprocess.run(["python", "admin_menu.py"])
        elif role == "Uzman":
            root.destroy()
            subprocess.run(["python", "main_menu.py"])
    else:
        # Hatalı giriş mesajını ekrana yaz
        error_label = tk.Label(error_frame, text="Hatalı bilgi girdiniz", font=("Helvetica", 12), fg="red",
                               bg="#f7f7f7")
        error_label.pack()


# Giriş alanlarını göstermek
def show_login(role):
    for widget in form_frame.winfo_children():  # Form çerçevesindeki mevcut widget'ları temizle
        widget.destroy()

    role_label = tk.Label(form_frame, text=f"{role} Girişi", font=("Helvetica", 16), fg="#555", bg="#f7f7f7")
    role_label.pack(pady=10)

    username_label = tk.Label(form_frame, text="Kullanıcı Adı:", font=("Helvetica", 14), bg="#f7f7f7", fg="#333")
    username_label.pack(pady=5)
    global username_entry
    username_entry = tk.Entry(form_frame, font=("Helvetica", 14), bd=1, relief="solid")
    username_entry.pack(pady=5)

    password_label = tk.Label(form_frame, text="Şifre:", font=("Helvetica", 14), bg="#f7f7f7", fg="#333")
    password_label.pack(pady=5)
    global password_entry
    password_entry = tk.Entry(form_frame, font=("Helvetica", 14), bd=1, relief="solid", show="*")
    password_entry.pack(pady=5)

    login_button = tk.Button(form_frame, text="Giriş Yap", font=("Helvetica", 14), bg="#0078D4", fg="white",
                             activebackground="#005bb5", activeforeground="white", relief="flat",
                             command=lambda: login(role))
    login_button.pack(pady=20)


# Ana pencereyi kapatma fonksiyonu
def on_closing():
    root.quit()  # Pencereyi kapat ve programı sonlandır


# Ana pencere
root = tk.Tk()
root.title("Giriş Sayfası")
root.geometry("1280x720")  # Masaüstü çözünürlüğü

# Pencereyi kapatma butonuna tıklandığında on_closing fonksiyonunu çağır
root.protocol("WM_DELETE_WINDOW", on_closing)

# Sol ve sağ bölge için çerçeveler
left_frame = tk.Frame(root, bg="#f7f7f7", width=640, height=720)
left_frame.pack(side=tk.LEFT, fill=tk.Y)

right_frame = tk.Frame(root, bg="#0078D4", width=640, height=720)
right_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Sol taraftaki giriş alanları
tk.Label(left_frame, text="Giriş Yap", font=("Helvetica", 24, "bold"), fg="#333", bg="#f7f7f7").pack(pady=20)

form_frame = tk.Frame(left_frame, bg="#f7f7f7")  # Dinamik giriş formu çerçevesi
form_frame.pack(pady=20)

# Hata mesajlarının gösterileceği çerçeve
error_frame = tk.Frame(left_frame, bg="#f7f7f7")
error_frame.pack(pady=10)

admin_button = tk.Button(left_frame, text="Admin Girişi", font=("Helvetica", 14), bg="#4CAF50", fg="white",
                         activebackground="#45A049", activeforeground="white", relief="flat",
                         command=lambda: show_login("Admin"))
admin_button.pack(pady=10)

uzman_button = tk.Button(left_frame, text="Uzman Girişi", font=("Helvetica", 14), bg="#0078D4", fg="white",
                         activebackground="#005bb5", activeforeground="white", relief="flat",
                         command=lambda: show_login("Uzman"))
uzman_button.pack(pady=10)

# Sağ tarafta "The Vision" yazısı
vision_font = Font(family="Helvetica", size=50, weight="bold")  # Font ayarı
tk.Label(right_frame, text="The Vision", font=vision_font, bg="#0078D4", fg="white").place(relx=0.5, rely=0.5,
                                                                                           anchor="center")

# Ana döngü
root.mainloop()
