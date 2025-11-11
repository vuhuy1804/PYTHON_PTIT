from math import log2

def solve(s, b):
    n = int(log2(b))
    if b == 2:
        print(s)
        return
    while len(s) % n != 0: s = '0' + s
    for i in range(0, len(s), n):
        res = 0
        for j in range(i, i + n):
            res = res * 2 + int(s[j])
        if res < 10: print(res, end = '')
        else: print(chr(ord('A') + res - 10), end = '')
    print()


f = open("DATA.in", "r")
t = int(f.readline())
for _ in range(t):
    b = int(f.readline())
    s = f.readline()
    s = s.strip()
    solve(s, b)
    