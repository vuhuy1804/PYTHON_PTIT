from math import *

p = [0] * 1000001

def sieve():
    for i in range(1000001): p[i] = 1
    p[0], p[1] = 0, 0
    for i in range(2, isqrt(100000)+1):
        if p[i]:
            for j in range(i*i, 1000001, i):
                p[j] = 0

sieve()
for _ in range(int(input())):
    n = int(input())
    a = []
    s = set()
    for i in range(2, n):
        j = int(str(i)[::-1])
        if i != j and j < n and p[i] and p[j] and i not in s:
            a.append([i, j])
            s.add(i)
            s.add(j)
    for x, y in a: print(x, y, end = ' ')
    print()