a, x = [], [0] * 20
res = []

def Try(i, st, sum, n):
    if sum > n:
        return
    for j in range(st, len(a)):
        if sum + a[j] <= n:
            x[i] = a[j]
            if sum + a[j] == n:
                s = '('
                for u in range(1, i + 1):
                    s += str(x[u])
                    if u != i:
                        s += ' '
                s += ')'
                res.append(s)
            else:
                Try(i + 1, j, sum + a[j], n)

t = int(input())
for _ in range(t):
    res.clear()
    a.clear()
    n = int(input())
    for i in range(n, 0, -1):
        a.append(i)
    Try(1, 0, 0, n)
    print(len(res))
    for s in res:
        print(s, end=' ')
    print()
