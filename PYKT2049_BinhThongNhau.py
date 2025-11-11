def Find(u, p):
    if u == p[u]: return u
    p[u] = Find(p[u], p)
    return p[u]

def Union(x, y):
    x = Find(x, p)
    y = Find(y, p)
    if x == y: return True
    p[y] = x
    return False

n = int(input())
N = 100001
p = [0] * N
for i in range(N): p[i] = i
for i in range(n):
    x, y, z = map(int, input().split())
    if z == 1: Union(x, y)
    else:
        x, y = Find(x, p), Find(y, p)
        print(1 if x == y else 0)
