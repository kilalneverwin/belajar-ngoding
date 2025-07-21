# import time

# t_start = time.time()

import sains.matematika
from sains import fisika
from sains.fisika import gaya as gy

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"Hasil tambah dari package adalah = {hasil_tambah}")

# t_end = time.time()

# print(f"waktu eksekusi adalah = {t_end - t_start}")

gaya = fisika.gaya(90,10)
print(f"gaya adalah {gaya}")

gaya = gy(90,10)
print(f"gaya adalah {gaya}")