f = open("profile.txt", "w")
name = input("Name : ")
age = input("Age : ")
f.write("Name : %s\n" % name)
f.write("Age : %s\n" % age)
f.close()