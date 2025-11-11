from math import *

def prime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return n > 1

def primedigit(n):
    sum = 0
    while n != 0:
        r = n % 10
        if r != 2 and r != 3 and r != 5 and r != 7: return False
        sum += r
        n //= 10
    return prime(sum)

for _ in range(int(input())):
    n = int(input())
    print('Yes' if primedigit(n) and prime(n) and prime(int(str(n)[::-1])) else 'No')