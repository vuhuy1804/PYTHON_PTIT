def DFS(u, adj, vs):
    vs[u] = 1
    for v in adj[u]:
        if vs[v] == 0:
            DFS(v, adj, vs)

def tplt(adj, vs):
    cnt = 0
    for i in range(1, n + 1):
        if vs[i] == 0:
            DFS(i, adj, vs)
            cnt += 1
    return cnt

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    vs = [0] * (n + 1)
    res = tplt(adj, vs) #so tplt ban dau
    tang = [0] * (n + 1)
    for i in range(1, n + 1):
        vs = [0] * (n + 1)
        vs[i] = 1
        tang[i] = tplt(adj, vs) - res
    maxx = max(tang)
    if maxx == 0: print(0)
    else:
        for i in range(1, n + 1):
            if tang[i] == maxx: print(i)

    

    
