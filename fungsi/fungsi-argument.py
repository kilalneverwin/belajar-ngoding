def cantik(nama):
	print(f"Selamat datang wahai cantikku {nama}")
	
cantik("oline")
cantik("Nina")


# fungsi tambah

def tambah(angka1,angka2):
	hasil = angka1 + angka2
	print(f"{angka1} + {angka2} = {hasil}")
	
tambah(8,1)
tambah(999,1)


def say_hi(list_member):
	data_member = list_member.copy()
	for member in data_member:
		print(f"Cantikku {member}")
		
member = ["Oline","Nina"]
say_hi(member)