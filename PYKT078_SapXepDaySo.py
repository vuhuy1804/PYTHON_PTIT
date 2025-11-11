t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    max_val, pos = -10**18, 0
    for i in range(n):
        if a[i] > max_val:
            max_val = a[i]
            pos = i
    a.insert(pos, m)
    b = []
    for x in a:
        if x < 0:
            b.append(x)
    for x in a:
        if x >= 0:
            b.append(x)
    for x in b:
        print(x, end = ' ')
    print()