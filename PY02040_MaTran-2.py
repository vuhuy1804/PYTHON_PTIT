n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
tren, duoi = 0, 0
for i in range(n):
    for j in range(n):
        if n - 1 - i < j: tren += a[i][j]
        elif n - 1 - i > j: duoi += a[i][j]
dis = abs(tren - duoi)
print('YES' if dis <= k else 'NO')
print(dis)