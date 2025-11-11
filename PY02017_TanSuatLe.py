t = int(input())
N = 10**6 + 1
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * N
    for x in a: cnt[x] += 1
    for i in range(N):
        if cnt[i] % 2 == 1:
            print(i)
            break
    t -= 1