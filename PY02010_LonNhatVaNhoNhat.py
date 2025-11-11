while True:
    n = int(input())
    if n == 0: break
    a = []
    for _ in range(n):
        s = input()
        while s[0] == '0' and len(s) > 1: s = s[1:]
        a.append(s)
    a.sort(key = lambda x : (len(x), x))
    if a[0] == a[-1]: print('BANG NHAU')
    else:
        print(a[0], a[-1])