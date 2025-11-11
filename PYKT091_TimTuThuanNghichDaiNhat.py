def check(s):
    t = s[::-1]
    return t == s

f = open('VANBAN.in', 'r')
d = dict()
max_len = 0
for s in f:
    a = s.split()
    for x in a:
        if check(x):
            if x not in d: d[x] = 1
            else: d[x] += 1
            max_len = max(max_len, len(x))
for x, y in d.items():
    if len(x) == max_len: print(x, y)