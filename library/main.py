import datetime

data_waktu = datetime.datetime.now()
print(f"Data waktu : {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","c","d","a","a","c","c"]
data_count = Counter(data)
print(data_count)
print(f"Jumlah A = {data_count['a']}")
print(f"Jumlah B = {data_count['b']}")
print(f"Jumlah C = {data_count['c']}")
print(f"Jumlah D = {data_count['d']}")

import io

file = io.open("library/text.txt","r")
print(file.read())