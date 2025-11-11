import math

t = int(input())
e = []
while True:
    try: e.extend(map(int, input().split()))
    except: break
I = 0
for _ in range(t):
    n, k = e[I:I+2]
    I+=2
    a = e[I:I+n]
    I+=n
    min_len = n + 1
    for i in range(0, n):
        uc = a[i]
        for j in range(i, n):
            uc = math.gcd(uc, a[j])
            if uc == k:
                min_len = min(min_len, j - i + 1)
                break
    print(min_len if min_len != n + 1 else -1)