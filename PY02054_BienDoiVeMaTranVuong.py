n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
st, cnt = (0 if n > m else 1), abs(m - n) - 1
d = []
if n != m:
    d.append(st)
    while cnt > 0:
        d.append(d[-1] + 2)
        cnt -= 1
if n > m:
    for i in range(n):
        if i not in d:
            for j in range(m):
                print(a[i][j], end = ' ')
            print()
else:
    for i in range(n):
        for j in range(m):
            if j not in d:
                print(a[i][j], end = ' ')
        print()