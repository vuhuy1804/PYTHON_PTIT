def check(n):
    s = str(n)
    if s != s[::-1]: return False
    se = set()
    for i in s:
        if (ord(i) - ord('0')) % 2 == 1: return False
        se.add(i)
    return len(se) % 2 == 1

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(22, n):
        if check(i): a.append(i)
    for i in range(len(a)):
        print(a[i], end = '')
        if i != len(a) - 1: print(' ', end = '')
    print()