n = int(input())
a = list(map(int, input().split()))
x = max(a)
cnt, ans = 0, 0
for i in a:
    if i == x:
        cnt += 1
        ans = max(ans, cnt)
    else: cnt = 0
print(ans)