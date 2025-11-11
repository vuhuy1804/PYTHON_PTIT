for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    maxx, minn = [0] * n, [10**9] * n
    minn[0], minn[-1], maxx[0], maxx[-1] = a[0], a[-1], a[0], a[-1]
    for i in range(1, n):
        maxx[i] = max(maxx[i-1], a[i])
    for i in range(n-2, 0, -1):
        minn[i] = min(minn[i+1], a[i])
    cnt = 0
    for i in range(n):
        if i == 0:
            if a[i] < minn[i+1]: cnt += 1
        elif i == n - 1:
            if a[i] >= maxx[i - 1]: cnt += 1
        else:
            if a[i] < minn[i+1] and a[i] >= maxx[i - 1]: cnt += 1
    print(cnt)
