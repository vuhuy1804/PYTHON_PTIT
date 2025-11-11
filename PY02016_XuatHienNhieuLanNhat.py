for _ in range(int(input())):
    cnt = [0] * 1000001
    lim = 0
    n = int(input())
    for i in map(int, input().split()):
        cnt[i] += 1
        lim = max(lim, i)
    res = max(cnt)
    ok = False
    for i in range(lim+1):
        if cnt[i] == res and cnt[i] > n//2:
            print(i)
            ok = True
            break
    if ok == False: print('NO')