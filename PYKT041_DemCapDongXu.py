n = int(input())
a = []
for i in range(n):
    a.append(input())
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            for i1 in range(i + 1, n):
                if a[i1][j] == 'C': cnt += 1
            for j1 in range(j + 1, n):
                if a[i][j1] == 'C': cnt += 1
print(cnt)
