from math import *

N = 10001
p = [1] * N
b = []

p[0], p[1] = 0, 0
for i in range(2, isqrt(N) + 1):
    if p[i] == 1:
        for j in range(i * i, N, i):
            p[j] = 0

for i in range(2, 10001):
    if p[i]: b.append(i)

n = int(input())
ans = 0
c = [int(x) for x in input().split()]
for i in c :
    s = 10**9
    for j in b :
        s = min(s, abs(i - j))
    ans = max(ans, s)
print(ans)