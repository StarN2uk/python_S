def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input())
s = is_prime_num(n)
print(s)