def check(n, p):
    cnt = 0
    for i in range(1, n + 1):
        res = i
        while res % p == 0:
            cnt += 1
            res //= p
    return cnt


t = int(input())
for i in range(t):
    n, p = map(int, input().split())
    print(check(n, p))