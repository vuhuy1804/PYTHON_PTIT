from math import *

def p(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
val = 0
for i in range(n):
    for j in range(m):
        if p(a[i][j]):
            val = max(val, a[i][j])
if val == 0: print('NOT FOUND')
else:
    print(val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == val:
                print(f'Vi tri [{str(i)}][{str(j)}]')