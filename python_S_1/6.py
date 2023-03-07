def number(num, s):
    if num % 2 == 0:
        s = 'even'
    else:
        s = 'odd'
    return s
num = int(input())
s = ""
n = number(num, s)
print(n)