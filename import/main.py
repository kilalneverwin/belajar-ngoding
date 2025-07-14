# import

# fungsinya adalah untuk mengambil program dari file internal .py

# contoh 1 untuk menyambng program
import program_print
import program_kilal

# contoh 2 import dengan data
import variabel
import fck

# data ada di namespace variabel
print(variabel.data)
print(fck.data)

# contoh 3 import dengan fungsi
import matematika

hasil = matematika.tambah(4,5)
print(hasil)