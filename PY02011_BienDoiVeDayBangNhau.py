n = int(input())
a = list(map(int, input().split()))
step, val = 1e9, 0
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += abs(a[i] - a[j])
    if cnt < step:
        step = cnt
        val = a[i]
print(step, val)