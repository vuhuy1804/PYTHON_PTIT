t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    n1, m1 = n - 2, m - 2
    a = [list(map(int, input().split())) for _ in range(n)]
    k = [list(map(int, input().split())) for _ in range(3)]
    res = 0
    for i in range(n1):
        for j in range(m1):
            s = 0
            for i1 in range(i, i + 3):
                for j1 in range(j, j + 3):
                    s += a[i1][j1] * k[i1 - i][j1 - j]
            res += s
    print(res)
    