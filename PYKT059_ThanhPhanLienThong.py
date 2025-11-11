def DFS(u, adj, vs):
    vs[u] = 1
    for v in adj[u]:
        if vs[v] == 0:
            DFS(v, adj, vs)

n, m, u = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
vs = [0] * (n + 1)
DFS(u, adj, vs)
ok = 0
for i in range(1, n + 1):
    if vs[i] == 0:
        ok = 1
        print(i)
if ok == 0: print(0)

    
