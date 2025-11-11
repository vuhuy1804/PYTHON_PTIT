t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key = lambda x : x[1])
    cnt, end = 1, a[0][1]
    for i in range(1, n):
        if a[i][0] >= end:
            end = a[i][1]
            cnt += 1
    print(cnt)