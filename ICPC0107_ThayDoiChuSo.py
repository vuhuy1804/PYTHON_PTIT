t = int(input())
for i in range(t):
    p, q = map(int, input().split())
    if p > q: p, q = q, p
    x1 = input()
    if len(x1.split()) > 1: x1, x2 = x1.split()
    else: x2 = input()
    m1, m2 = '', ''
    for c in x1:
        if c == str(q): m1 += str(p)
        else: m1 += c
    for c in x2:
        if c == str(q): m2 += str(p)
        else: m2 += c
    print(int(m1) + int(m2), end = ' ')
    m1, m2 = '', ''
    p, q = q, p
    for c in x1:
        if c == str(q): m1 += str(p)
        else: m1 += c
    for c in x2:
        if c == str(q): m2 += str(p)
        else: m2 += c
    print(int(m1) + int(m2))
