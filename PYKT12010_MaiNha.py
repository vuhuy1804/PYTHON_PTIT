n = int(input())
a = list(map(int, input().split()))
b = a.copy()
ans = 10**9
for i in range(n):
    res = 0
    for l in range(i, 0, -1):
        res += abs(a[l] - 1 - a[l-1])
        a[l-1] = a[l] - 1
    for r in range(i, n-1):
        res += abs(a[r] - 1 - a[r+1])
        a[r+1] = a[r] - 1
    ans = min(ans, res)
    a = b.copy()
print(ans)