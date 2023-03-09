def plus(a, c):
    n = int(a) + int(c)
    return n
def minus(a, c):
    n = int(a) - int(c)
    return n
def multiply(a, c):
    n = int(a) * int(c)
    return n
def divide(a, c):
    n = int(a) // int(c)
    return n
n = ''
a, b, c = input().split()
if b == '+':
    n = plus(a, c)
elif b == '-':
    n = minus(a, c)
elif b == '*':
    n = multiply(a, c)
elif b == '//':
    n = divide(a, c)
print("{0} {1} {2} = {3}".format(a, b, c, n))