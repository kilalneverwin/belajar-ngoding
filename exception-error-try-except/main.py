# contoh sederhana menangkap exception
from math import nan

#input_user = int(input("masukkan angka : "))
#hasil = nan

#try:
#    hasil = 10/input_user
#except:
#    print("Gak bisa pakai nol")

#print(f"Hasil = {hasil}")

# contoh di aplikasi

while(True):
    angka = int(input("masukkan angka pembagi : "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("mau lagi (y/n)? ")
        if is_done == "n":
            break
    except:
        print("Pembagi nol, silahkan ulang")

print("akhir dari program 1")

# contoh aplikasi untuk membuat file data.txt

try:
    with open("data.txt", 'r') as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt",'w',encoding='utf-8') as file:
        file.write("file baru")

print("akhir dari program 2")