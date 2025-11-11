t = int(input())
while t > 0:
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d1, d2, d3 = dict(), dict(), dict()
    for x in a:
        if x in d1: d1[x] += 1
        else: d1[x] = 1
    for x in b:
        if x in d2: d2[x] += 1
        else: d2[x] = 1
    for x in c:
        if x in d3: d3[x] += 1
        else: d3[x] = 1
    ok = 0
    for x in a:
        if x not in d2 or x not in d3: continue
        fre = min(d1[x], d2[x], d3[x])
        #print(x, fre)
        if fre > 0:
            ok = 1
            while fre > 0:
                print(x, end = ' ')
                fre -= 1
            d2[x], d3[x] = 0, 0
    if ok == 0: print('NO')
    else: print()
    t -= 1