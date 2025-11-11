from math import *

def p(n):
    if n < 10: return False
    rev, tmp = 0, n
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == tmp

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
val = -1
for i in range(n):
    for j in range(m):
        if p(a[i][j]):
            val = max(val, a[i][j])
if val == -1: print('NOT FOUND')
else:
    print(val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == val:
                print(f'Vi tri [{str(i)}][{str(j)}]')