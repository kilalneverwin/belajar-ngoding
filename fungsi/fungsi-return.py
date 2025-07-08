# kuadrat

def kuadrat(input_kuadrat):
	output_kuadrat = input_kuadrat**2
	return output_kuadrat
	
y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(5)
print(z)

# fungsi tambah

def fungsi_tambah(angka1,angka2):
	return angka1+angka2

a = fungsi_tambah(5,5)
print(a)

# fungsi return banyak

def fungsi_matematika(angka_1,angka_2):
	tambah = angka_1 + angka_2
	kurang = angka_1 - angka_2
	bagi = angka_1 / angka_2
	kali = angka_1 * angka_2
	
	return tambah,kurang,bagi,kali
	
k,l,m,n = fungsi_matematika(5,3)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil bagi = {m}")
print(f"Hasil kali = {n}")