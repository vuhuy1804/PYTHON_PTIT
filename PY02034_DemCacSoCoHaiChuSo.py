n = input()
d = dict()
i = 0
while i < len(n):
    t = n[i:i+2]
    if len(t) < 2: break
    if t not in d: d[t] = 1
    else: d[t] += 1
    i += 2
for x, y in d.items(): print(x, y)