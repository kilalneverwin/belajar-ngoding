# __main___

# __name__ == "__main__" akan terjadi di program utama

# __name__ pada file program utama
print(f"Nilai __name__ pada main.py = '{__name__}'")

# __name__ pada file program eksternal
import lalz

# deklarasi
def fungsi_tambah(a:int,b:int) ->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")

# import package
import package