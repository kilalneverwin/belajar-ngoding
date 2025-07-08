# contoh 1

def say_hi(nama = "Nina"):
	print(f"Hallo {nama}")
	
say_hi("oline")
say_hi()

# contoh 2

def sapa_dia(nama,pesan = "Tamvan"):
	print(f"Hallo {nama}, {pesan}")
	
sapa_dia("Dicky","Ganteng")
sapa_dia("Pebrayen")

# contoh 3

def hitung_pangkat(angka,pangkat=2):
	hasil = angka**pangkat
	return hasil
	
print(hitung_pangkat(2,4))

hasil = hitung_pangkat(angka=5, pangkat=3)
print(hasil)

# contoh 4

def tambah(input1=1,input2=2,input3=3,input4=4):
	hasil = input1+input2+input3+input4
	return hasil
	
print(tambah())
print(tambah(input1=2))