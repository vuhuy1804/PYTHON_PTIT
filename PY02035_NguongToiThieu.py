n = input()
k = int(input())
d = dict()
i = 0
while i < len(n):
    t = n[i:i+2]
    if len(t) < 2: break
    if t not in d: d[t] = 1
    else: d[t] += 1
    i += 2
a = sorted(list(d.items()))
ok = 0
for x, y in a:
    if y >= k:
        print(x, y)
        ok = 1
if ok == 0: print('NOT FOUND')