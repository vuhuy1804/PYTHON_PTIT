for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [1] * n
    for i in range(n):
        j = i - 1
        while j >= 0:
            if (a[j] <= a[i]):
                b[i] += b[j]
                j -= b[j]
            else: break
    for x in b: print(x, end = ' ')
    print()
