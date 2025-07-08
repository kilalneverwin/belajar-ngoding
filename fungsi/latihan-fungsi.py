import os

#os.system("clear")
# os.system("cls")

# membuat header

#print(f"{'PROGRAM MENGHITUNG LUAS' : ^40}")
#print(f"{'DAN KELILING PERSEGI' :^40}")
#print(f"{'-'*40 :^40}")

# mengambil input
#PANJANG = int(input("Masukkan panjang persegi : "))
#LEBAR = int(input("Masukkan lebar persegi : "))

# menghitung

#LUAS = PANJANG*LEBAR
#KELILING = 2*(PANJANG+LEBAR)

# menampilkan hasil

#print(f"Hasil perhitungan luas = {LUAS}")
#print(f"Hasil perhitungan keliling = {KELILING}")

# fungsi fungsinya disini

def header():
	print(f"{'PROGRAM MENGHITUNG LUAS' : ^40}")
	print(f"{'DAN KELILING PERSEGI' :^40}")
	print(f"{'-'*40 :^40}")
	

def input_user():
	panjang = int(input("Masukkan panjang persegi : "))
	lebar = int(input("Masukkan lebar persegi : "))
	
	return panjang,lebar

def hitung_luas(panjang,lebar):
	return panjang*lebar
	
def hitung_keliling(panjang,lebar):
	return 2*(panjang+lebar)
	
def display(pesan,value):
	print(f"Hasil perhitungan {pesan} {value}")

# program utamanya

while True:
	header()
	PANJANG,LEBAR = input_user()
	LUAS = hitung_luas(PANJANG,LEBAR)
	KELILING = hitung_keliling(PANJANG,LEBAR)
	display("luas", LUAS)
	display("keliling", KELILING)
	
	isContinue = input("Mau lanjut (y/n) ?")
	if isContinue == "n":
		break
		
print("Program Selesai Thx")