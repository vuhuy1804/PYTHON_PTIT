def DFS(u, adj, vs):
    vs[u] = 1
    for v in adj[u]:
        if vs[v] == 0:
            DFS(v, adj, vs)

t = int(input())
for _ in range(t):
    n, m, u, v = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
    cnt = 0
    for i in range(1, n + 1):
        if i == u or i == v: continue
        vs = [0] * (n + 1)
        vs[i] = 1
        DFS(u, adj, vs)
        if vs[v] == 0: cnt += 1
    print(cnt)

    
