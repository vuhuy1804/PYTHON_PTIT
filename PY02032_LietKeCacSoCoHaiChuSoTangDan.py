n = input()
s = set()
i = 0
while i < len(n):
    t = n[i:i+2]
    if len(t) < 2: break
    s.add(int(t))
    i += 2
s = sorted(list(s))
for x in s: print(x, end = ' ')