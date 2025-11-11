for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    ok = True
    for i in range(n):
        if a[i] > b[i]:
            ok = False
            break
    print('YES' if ok else 'NO')