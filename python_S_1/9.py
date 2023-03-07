def get_sum(n):
    s = 0
    m = 0
    for i in range(1, n + 1):
        m = int(input())
        if m >= s:
            s = m
    return s
n = int(input("Enter integer n : "))
max = get_sum(n)
print("max value :", max)