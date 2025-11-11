X = []
a = []
def Try(i, st, n, k):
    for j in range(st, n - k + i):
        X.append(a[j])
        if i == k:
            for x in X: print(x, end = ' ')
            print()
        else: Try(i + 1, j + 1, n, k)
        X.pop()
n, k = map(int, input().split())
a = sorted(list(set(input().split())))
Try(1, 0, len(a), k)