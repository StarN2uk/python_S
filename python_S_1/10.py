def rect(w, h):
    return w * h
def tri(w, h):
    return w * h / 2
def circle(r):
    return r ** 2 * 3.14
print("Choose a shape : ")
print("1. Rectangle", "2. Triangle", "3. Circle", sep = '\n')
n = int(input())
if n == 1:
    w = int(input("width : "))
    h = int(input("height : "))
    area = rect(w, h)
elif n == 2:
    w = int(input("width : "))
    h = int(input("height : "))
    area = tri(w, h)
elif n == 3:
    r = int(input("radius : "))
    area = circle(r)
print(area)