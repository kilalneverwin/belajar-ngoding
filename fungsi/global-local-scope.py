## global dan local scope

nama_global = "Oline" # <- ini adalah variabel global

# akses variabel global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan nama {nama_global}")

fungsi1()

#  akses variabel global dalam loop

for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabagan

if True:
    print(f"if menampilkan {nama_global}")

# variabel local scope

def fungsi2():
    nama_local = "Nina" # ini adalah variabel lokal scope

fungsi2()
# print(nama_local) <- teu bisa bossqueee

# contoh 1 penggunaan

def say_erine():
    print(f"hallo {nama}")

nama = "erine"
say_erine()

# contoh 2 merubah variabel

angka = 0
name = "lily"

def ubah(nilai_baru,nama_baru):
    global angka # <- fungsi ini mendapat akses merubah angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f"sebelum {angka,name}")
ubah(10, "delynn")
print(f"sesudah {angka,name}")


# contoh 3

angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)