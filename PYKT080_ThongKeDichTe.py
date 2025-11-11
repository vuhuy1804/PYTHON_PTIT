a = [[0 for _ in range(105)] for _ in range(105)]
q = []
dx = [-1, 1, 0, 0, -1,  -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
n, m, cnt = 0, 0, 0

def DFS(i, j):
    global cnt
    for k in range(8):
        i1, j1 = i + dx[k], j + dy[k]
        if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m and a[i1][j1] != 0:
            cnt += a[i1][j1]
            a[i1][j1] = 0

n, m = map(int, input().split())
for i in range(n):
    a[i] = list(map(int, input().split()))
    for j in range(m):
        if a[i][j] == -1:
            q.append([i, j])
while len(q) > 0:
    u = q[0]
    q.pop(0)
    DFS(u[0], u[1])
print(cnt)