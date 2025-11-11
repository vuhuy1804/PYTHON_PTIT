from math import *
N = 10**6+1
p = [0] * N

for i in range(N): p[i] = 1
p[0], p[1] = 0, 0
for i in range(2, isqrt(N)+1):
    if p[i]:
        for j in range(i*i, N, i):
            p[j] = 0

n = int(input())
a = list(map(int, input().split()))
d = dict()
for x in a:
    if p[x]:
        if x not in d: d[x] = 1
        else: d[x] += 1
for x, y in d.items(): print(x, y)