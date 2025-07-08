import random

angka_rahasia = random.randint(1, 100)
ronde = 0
max_ronde = 5

print("===== TEBAK ANGKA =====")
print("Pilih angka dari 1 sampe 100")
print(f"Ente punya {max_ronde} kesempatan")

while(ronde < max_ronde):
	tebakan = int(input("Masukin tebakan ente : "))
	ronde += 1
	
	if tebakan < angka_rahasia:
		print("Jawaban ente terlalu kecil")
	elif tebakan > angka_rahasia:
		print("Jawaban ente terlalu besar")
	else:
		print("Horee, jawaban ente betul")
		exit(0)
print("Makasih udah bermain")
print(f"Jawabannya --> {angka_rahasia} <--")