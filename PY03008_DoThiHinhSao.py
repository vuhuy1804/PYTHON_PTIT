n = int(input())
cnt = [0] * (n + 1)
for i in range(n - 1):
    x, y = map(int, input().split())
    cnt[x] += 1
    cnt[y] += 1
ok = 0
for x in cnt:
    if x == n - 1:
        ok = 1
        break
print('Yes' if ok else 'No')