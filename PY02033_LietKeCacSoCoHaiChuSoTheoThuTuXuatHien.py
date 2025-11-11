n = input()
s = set()
i = 0
while i < len(n):
    t = n[i:i+2]
    if len(t) < 2: break
    if t not in s: 
        print(t, end = ' ')
        s.add(t)
    i += 2