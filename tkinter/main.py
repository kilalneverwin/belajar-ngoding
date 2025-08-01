import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="black")
window.geometry("300x200")
window.resizable(False,False)
window.title("Kilal ganteng")

# variabel dan input
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, cantik atau ganteng"
    showinfo(title="Wassap mamen",message=pesan)

# frame input

input_frame = ttk.Frame(window)

# penempatan grid,pack, place
# x=horizontal y=vertikal

# komponen komponen
# 1. label nama depan
input_frame.pack(padx=10,pady=10,fill="x",expand="True")
nama_depan_label = ttk.Label(input_frame,text="Nama depan : ")
nama_depan_label.pack(padx=10,fill="x",expand="True")

# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand="True")

# 3. label nama depan
input_frame.pack(padx=10,pady=10,fill="x",expand="True")
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang : ")
nama_belakang_label.pack(padx=10,fill="x",expand="True")

# 4. entry nama depan
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand="True")

# 5. tombol

tombol_sapa = ttk.Button(input_frame,text="Sapa gue!",command=tombol_click)
tombol_sapa.pack(padx=10,pady=10,fill="x",expand="True")

# main loop windows
window.mainloop()