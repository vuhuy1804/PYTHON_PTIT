from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

def sumdigit(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

for _ in range(int(input())):
    a, b = map(int, input().split())
    uc = gcd(a, b)
    print("YES" if prime(sumdigit(uc)) else "NO")