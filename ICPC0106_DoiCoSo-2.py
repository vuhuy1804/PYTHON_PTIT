from math import log2

def convert(n, b):
    cs = int(log2(b))
    while len(n) % cs != 0: n = '0' + n
    for i in range(0, len(n), cs):
        s = 0
        for j in range(i, i + cs): s = 2 * s + int(n[j])
        print(s if s < 10 else chr(ord('A') + s - 10), end = '')

t = int(input())
for i in range(t):
    b = int(input())
    n = input()
    convert(n, b)
    print()