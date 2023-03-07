def get_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += int(input())
    return s
n = int(input("Enter integer n : "))
sum = get_sum(n)
print("sum : ", sum)