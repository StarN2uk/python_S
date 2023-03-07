def Login(id, password, a, b):
    result = 0
    if id == a and password == b:
        result = 1
    elif id == a:
        result = 2
    elif password == b:
        result = 3
    else:
        result = 4
    return result
id = 'Cube'
password = '1234'
a = input("ID : ")
b = input("PW : ")
x = Login(id, password, a, b)
if x == 1:
    print("Login Success")
elif x == 2:
    print("Please check your PW")
elif x == 3:
    print("Please check your ID")
else:
    print("Please check ID and PW")