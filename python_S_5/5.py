f = open("example.txt", "r")
data = f.readlines()
for line in data :
    print(line, end = '')
f.close()