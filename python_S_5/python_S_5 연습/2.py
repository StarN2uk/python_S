def read_file(file_name):
    f = open(file_name, "r")
    line = f.readlines()
    print(line)
def write_file(file_name):
    f = open(file_name, "w")
    Name = input("Name : ")
    Age = input("Age : ")
    f.write("Name : %s\n" % Name)
    f.write("Age : %s\n" % Age)
file_name = input("File name : ")
mode = input("File mode(r/w/a) : ")
if mode == "r":
    read_file(file_name)
else :
    write_file(file_name)