import sains
from sains.matematika import scientific

hasil_tambah = sains.matematika.tambah(1,2,3,4,45)
print(f"Hasil tambah = {hasil_tambah}")

hasil_fisika = sains.fisika.gaya(10,9.8)
print(f"Hasil fisika = {hasil_fisika}")

hasil_kali = sains.matematika.kali(1,3,4,5,6)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
print(f"Hasil pangkat 3 = {pangkat_3(5)}")


#from sains import *

#hasil_tambah = matematika.basic.tambah(1,2,3,4,45)
#print(f"Hasil tambah = {hasil_tambah}")

#hasil_fisika = fisika.gaya(10,9.8)
#print(f"Hasil fisika = {hasil_fisika}")

#hasil_kali = matematika.basic.kali(1,3,4,5,6)
#print(f"Hasil kali = {hasil_kali}")