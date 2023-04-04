f = open("alphabet.txt", "r")
index = int(input("index : "))
f.seek(index)
for i in range(index, 26):
    a = f.readline()
    print(a)
f.close()