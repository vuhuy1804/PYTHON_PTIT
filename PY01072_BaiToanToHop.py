x = [0] * 100

def Try(i, n, k):
    for j in range(x[i-1]+1, n-k+i+1):
        x[i] = j
        if i == k:
            for u in range(1, k+1): print(a[x[u]-1], end = ' ')
            print()
        else: Try(i+1, n, k)

n, k = map(int, input().split())
a = sorted(list(set(map(int, input().split()))))
n = len(a)
Try(1, n, k)
