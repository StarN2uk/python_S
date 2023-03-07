def square(a, b, s):
    for i in range(1, b + 1):
        if i == b:
            return s
        s = s * a
a = int(input())
b = int(input())
s = a
n = square(a, b, s)
print(n)