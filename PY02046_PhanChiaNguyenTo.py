from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = list(map(int, input().split()))
s = set()
b = []
for x in a:
    if x not in s:
        b.append(x)
        s.add(x)
n = len(b)
f = [0] * n
f[0] = b[0]
for i in range(1, n):
    f[i] = f[i - 1] + b[i]
ok = 0
for i in range(n - 1):
    l, r = f[i], f[n - 1] - f[i]
    if prime(l) and prime(r):
        print(i)
        ok = 1
        break
if ok == 0:
    print('NOT FOUND')