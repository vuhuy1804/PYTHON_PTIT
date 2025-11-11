import sys
sys.setrecursionlimit(10**6)

def DFS(u, adj, color):
    color[u] = 1
    for v in adj[u]:
        if color[v] == 0:
            if DFS(v, adj, color):
                return True
        elif color[v] == 1:
            return True
    color[u] = 2
    return False

cnt, d, a = 1, dict(), []
n = int(input())
for _ in range(n):
    line = input()
    a.append(line)
    x, s, y = line.split()
    if x not in d:
        d[x] = cnt
        cnt += 1
    if y not in d:
        d[y] = cnt
        cnt += 1

adj = [[] for _ in range(cnt + 1)]
color = [0] * (cnt + 1)

for line in a:
    x, s, y = line.split()
    if s == '>':
        adj[d[x]].append(d[y])
    else:
        adj[d[y]].append(d[x])

ok = False
for i in range(1, cnt + 1):
    if color[i] == 0:
        if DFS(i, adj, color):
            ok = True
            break

print('impossible' if ok else 'possible')