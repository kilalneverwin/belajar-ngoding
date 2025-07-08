def fungsi_biasa(nama,tinggi,berat):
	print(f"{nama} punya tinggi badan {tinggi} dan berat badan {berat}")
	
fungsi_biasa("Nala",165,55)

def fungsi_kwargs(**kwargs):
	nama = kwargs["nama"]
	tinggi = kwargs["tinggi"]
	berat = kwargs["berat"]
	print(f"{nama} punya tinggi badan {tinggi} dan berat badan {berat}")
	
fungsi_kwargs(nama="Nala",tinggi=165,berat=55)

# studi kasus

def math(*args,**kwargs):
	output = 0
	if kwargs["option"] == "tambah":
		for angka in args:
			output += angka
	elif kwargs["option"] == "kali":
		output = 1
		for angka in args :
			output *= angka
	else:
		print("kagak ada operasi blok!!")
		
	return output
	
	
	
hasil = math(1,2,3,4,option="tambah")
print(f"hasil jumlah = {hasil}")

hasil = math(1,2,3,4,option="kali")
print(f"hasil kali = {hasil}")