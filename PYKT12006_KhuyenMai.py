n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(n):
    c.append([a[i], b[i]])
c.sort(key = lambda x : (x[0] - x[1]))
res = 0
for i in range(k): res += c[i][0]
i = k
while i < n and c[i][0] < c[i][1]:
    res += c[i][0]
    i += 1
for j in range(i, n): res += c[j][1]
print(res)