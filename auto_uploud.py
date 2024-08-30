import pyautogui
import time
import random
import tkinter as tk
from tkinter import ttk
import threading

# Variabel untuk kontrol threading
running = False

def run_bot():
    global running
    running = True
    day = day_var.get()
    time_of_day = time_var.get()
    
    links = {
        'Senin': {
            'Pagi': [
                'https://www.facebook.com/groups/452512229583913',
                'https://www.facebook.com/groups/646832658764868'
            ],
            'Siang': [
                'https://www.facebook.com/groups/183304072340276',
                'https://www.facebook.com/groups/1344335369285894'
            ],
            'Malam': [
                'https://www.facebook.com/groups/komunitassupirtrukindonesia'
            ]
        },
        'Rabu': {
            'Pagi': [
                'https://www.facebook.com/groups/185880505117882',
                'https://www.facebook.com/groups/776837162422332'
            ],
            'Siang': [
                'https://www.facebook.com/groups/868335030388905'
            ],
            'Malam': [
                'https://www.facebook.com/groups/1452981858164617'
            ]
        },
        'Jumat': {
            'Pagi': [
                'https://www.facebook.com/groups/452512229583913',
                'https://www.facebook.com/groups/183304072340276'
            ],
            'Siang': [
                'https://www.facebook.com/groups/komunitassupirtrukindonesia',
                'https://www.facebook.com/groups/185880505117882'
            ],
            'Malam': [
                'https://www.facebook.com/groups/646832658764868',
                'https://www.facebook.com/groups/1344335369285894'
            ]
        },
        'Minggu': {
            'Pagi': [
                'https://www.facebook.com/groups/776837162422332'
            ],
            'Siang': [
                'https://www.facebook.com/groups/868335030388905'
            ],
            'Malam': [
                'https://www.facebook.com/groups/1452981858164617',
                'https://www.facebook.com/groups/185880505117882'
            ]
        }
    }

    captions = {
        'Senin': "Awali minggu dengan langkah pasti! 🚛 Butuh bantuan? Saya siap membantu dengan cepat dan rapi. Hubungi WA: 085183107469. Privasi terjaga, hasil memuaskan.",
        'Rabu': "Sedang di perjalanan jauh atau dalam antrean panjang? Jangan khawatir, saya bisa bantu urusan kecil Anda dengan cepat. WA: 085183107469. Hasil pasti, privasi aman.",
        'Jumat': "Persiapkan minggu depan dengan tenang. Biar saya bantu urusan Anda hari ini. WA: 085183107469. Proses cepat, hasil memuaskan, privasi dijamin.",
        'Minggu': "Nikmati akhir pekan tanpa khawatir! Kalau ada urusan yang perlu dibantu, saya siap sedia. WA: 085183107469. Cepat, rapi, dan privasi terjaga."
    }
    
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)

    for link in links[day][time_of_day]:
        if not running:
            break  # Keluar dari loop jika running diubah menjadi False

        pyautogui.click(770, 105)
        time.sleep(1)

        pyautogui.write(link)
        pyautogui.press('enter')
        time.sleep(random.uniform(10, 20))

        time.sleep(30)

        pyautogui.write(captions[day])
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(random.uniform(1, 2))

        pyautogui.click(950, 962)
        time.sleep(random.uniform(10, 20))

        if len(links[day][time_of_day]) > 1 and link != links[day][time_of_day][-1]:
            pyautogui.hotkey('ctrl', 't')
            time.sleep(1)

def stop_bot():
    global running
    running = False  # Menghentikan loop di dalam fungsi run_bot

# Setup GUI
root = tk.Tk()
root.title("Facebook Group Post Automation")

# Variabel untuk pilihan hari dan waktu
day_var = tk.StringVar(value='Senin')
time_var = tk.StringVar(value='Pagi')

# Dropdown untuk memilih hari
ttk.Label(root, text="Pilih Hari:").grid(column=0, row=0, padx=10, pady=10)
day_menu = ttk.Combobox(root, textvariable=day_var, values=['Senin', 'Rabu', 'Jumat', 'Minggu'])
day_menu.grid(column=1, row=0, padx=10, pady=10)

# Dropdown untuk memilih waktu
ttk.Label(root, text="Pilih Waktu:").grid(column=0, row=1, padx=10, pady=10)
time_menu = ttk.Combobox(root, textvariable=time_var, values=['Pagi', 'Siang', 'Malam'])
time_menu.grid(column=1, row=1, padx=10, pady=10)

# Tombol untuk menjalankan bot
run_button = ttk.Button(root, text="Run", command=lambda: threading.Thread(target=run_bot).start())
run_button.grid(column=0, row=2, padx=10, pady=20)

# Tombol untuk menghentikan bot
stop_button = ttk.Button(root, text="Stop", command=stop_bot)
stop_button.grid(column=1, row=2, padx=10, pady=20)

root.mainloop()
