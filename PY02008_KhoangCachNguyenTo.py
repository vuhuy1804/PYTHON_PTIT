from math import *

def prime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return n > 1

n, x = map(int, input().split())
a = [x for x in range(2, 10000) if prime(x)]
print(x, end = ' ')
for i in range(n):
    x += a[i]
    print(x, end = ' ')