def factorial(n):
    if n == 1:
        return 1
    else :
        return n * factorial(n - 1)
fac = factorial(4)
print("4! =", fac)