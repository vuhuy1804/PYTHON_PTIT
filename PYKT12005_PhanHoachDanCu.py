t = int(input())
for _ in range(t):
    n, c, d = map(int, input().split())
    if c > d: c, d = d, c #coi c nho hon d
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s1, s2 = sum(a[:c]) / c, sum(a[c:c+d]) / d
    print('%.6f' % (s1 + s2))