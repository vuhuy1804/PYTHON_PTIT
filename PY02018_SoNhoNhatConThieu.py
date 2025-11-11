cnt = [0] * 30002
n = int(input())
a = list(map(int, input().split()))
for x in a: cnt[x] += 1
for i in range(1, 30002):
    if cnt[i] == 0:
        print(i)
        break