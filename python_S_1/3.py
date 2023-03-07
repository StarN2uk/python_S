def get_add(x, y, z):
    for i in range(x, y + 1):
        z += i
    return z
x = int(input())
y = int(input())
z = 0
a = get_add(x, y, z)
print("{0}부터 {1}까지의 합은 {2}입니다.".format(x, y, a))