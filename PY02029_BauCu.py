n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * (m + 1)
for x in a: cnt[x] += 1
max1, max2, res = -1, -1, 0
max1 = max(cnt)
for i in range(m + 1):
    if cnt[i] < max1 and cnt[i] > max2:
        max2 = cnt[i]
        res = i
if res == 0: print('NONE')
else: print(res)