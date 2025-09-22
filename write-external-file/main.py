# 1 mode write

# bakal ketimpa

with open("data-1.txt",'w',encoding="utf-8") as file:
    file.write("kehidupan ajg")


# 2 mode append
with open("data-2.txt",'w',encoding="utf-8") as file:
    file.write("kehidupan ajg\n")

with open("data-2.txt",'a',encoding="utf-8") as file:
    file.write("anjing lah")

# 3 mode r+

with open("data-3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("data-3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")

with open("data-3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data-3.txt",'r+',encoding="utf-8") as file:
    file.write("asu surasu")