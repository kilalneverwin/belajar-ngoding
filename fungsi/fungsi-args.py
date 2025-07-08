# args

def fungsi(*args):
	nama = args[0]
	tinggi = args[1]
	berat = args[2]
	
	print(f"{nama} tingginya {tinggi} dan berat nya {berat}")
	
fungsi("Oline",170,50)

# contoh lain

def tambah(*data):
	output = 0
	for angka in data:
		output += angka
	
	return output

hasil = tambah(1,2,3,4,5)
print(f"hasil {hasil}")

hasil = tambah(10,100)
print(f"hasil {hasil}")