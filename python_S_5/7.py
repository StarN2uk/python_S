f = open("profile.txt", "a")
school = input("school : ")
f.write("School : %s\n" % school)
f.close()