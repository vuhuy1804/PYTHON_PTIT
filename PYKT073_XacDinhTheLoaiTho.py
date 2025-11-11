n = int(input())
a = [list(input().split()) for _ in range(n)]
ans = []
idx = 0
while idx < n:
    ok = 0
    if len(a[idx]) == 6:
        ok = 1
        while idx < n and len(a[idx]) == 6:
            idx += 2
    else:
        ok = 2
        idx += 4
    ans.append(ok)
print(len(ans))
for x in ans:
    print(x)