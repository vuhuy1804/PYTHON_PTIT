from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))
p = []
for i in range(n):
    if prime(a[i]):
        p.append(a[i])
        a[i] = 0
p.sort(reverse=True)
for x in a:
    if x == 0:
        print(p[-1], end = ' ')
        p.pop()
    else: print(x, end = ' ')

