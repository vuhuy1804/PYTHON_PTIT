n = int(input())
a = []
for i in range(n):
    s = input()
    t = ''
    for c in s:
        if c.isdigit(): t += c
        else: t += ' '
    b = t.split()
    for x in b:
        while x[0] == '0' and len(x) > 1: x = x[1:]
        a.append(x)
a.sort(key = lambda x : (len(x), x))
for x in a: print(x)