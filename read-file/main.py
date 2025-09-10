# tutorial membaca file eksternal

print(3*"="," Membaca File Txt ",3*"=")
file = open("read-file/data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

# baca semua baris
print(file.read())

# baca satu persatu
# print(file.readline(),end="") # baris pertama
# print(file.readline(),end="") # baris selanjutnya

# baca semua baris sebagai lines
# print(file.readlines())

print(f"apakah file sudah di close : {file.closed}")

file.close()
print(f"apakah file sudah di close : {file.closed}")

# salah satu teknik membuka file di python
print("\n",3*"="," Membaca File Txt ",3*"=")

with open("read-file/data.txt",mode="r") as file:
    konten = file.readline()
    print(konten,end="")
    print(f"apakah file sudah di close : {file.closed}")

print(f"apakah file sudah di close : {file.closed}")
