for _ in range(int(input())):
    cnt = [0] * 1001
    for i in range(int(input())):
        cnt[int(input())] += 1
    res = max(cnt)
    for i in range(1001):
        if cnt[i] == res:
            print(i)
            break