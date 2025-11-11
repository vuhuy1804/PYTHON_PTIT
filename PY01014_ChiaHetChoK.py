a, k, n = map(int, input().split())
lim, st = n - a, k - (a % k)
ok = False
while st <= lim:
    ok = True
    print(st, end = ' ')
    st += k
if ok == False: print(-1)
