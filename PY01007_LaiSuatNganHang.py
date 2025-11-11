for _ in range(int(input())):
    n, x, m = map(float, input().split())
    cnt = 0
    while n < m:
        cnt += 1
        n += n * x / 100
    print(cnt)