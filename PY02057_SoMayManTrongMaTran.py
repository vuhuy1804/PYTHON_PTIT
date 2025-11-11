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
maxx, minn = 0, 10**9
for i in range(n):
    for j in range(m):
        maxx = max(maxx, a[i][j])
        minn = min(minn, a[i][j])
val = maxx - minn
ok = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == val:
            ok = 1
if ok == 0: print('NOT FOUND')
else:
    print(val)
    for i in range(n):
        for j in range(m):
            if a[i][j] == val:
                ok = 1
                print(f'Vi tri [{str(i)}][{str(j)}]')