f = open("profile.txt", "r")
data = f.readlines()
print(data[2])
f.close()