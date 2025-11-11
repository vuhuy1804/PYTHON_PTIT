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
    cnt = 0
    for i in range(5, n - 6):
        if p[i] and p[i+2] and p[i+6]: cnt += 1
        if p[i] and p[i+4] and p[i+6]: cnt += 1
    print(cnt)