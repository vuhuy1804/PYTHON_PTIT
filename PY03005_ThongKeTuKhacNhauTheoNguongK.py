n, k = map(int, input().split())
d = dict()
for i in range(n):
    s = input().lower()
    t = ''
    for c in s:
        if c.isalpha() or c.isdigit(): t += c
        else: t += ' '
    a = t.split()
    for x in a:
        if x not in d: d[x] = 1
        else: d[x] += 1
b = list(d.items())
b.sort(key = lambda x : (-x[1], x[0]))
for x, y in b:
    if y >= k: print(x, y)
    else: break