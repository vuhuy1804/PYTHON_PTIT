for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    ok = True
    for i in range(len(a)):
        if a[i] not in d: d[a[i]] = i
        else:
            if i - d[a[i]] < n - 1:
                ok = False
                break
            else: d[a[i]] = i
    print('YES' if ok else 'NO')