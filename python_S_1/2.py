def get_max(x, y):
    if x > y:
        return x
    else:
        return y
x = int(input())
y = int(input())
n = get_max(x, y)
print(n)