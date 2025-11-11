def check(s):
    for c in s:
        if not c.isdigit(): return True
    return len(s) > 18

f = open('DATA.in', 'r')
a = []
for s in f:
    b = s.split()
    for x in b:
        if check(x): a.append(x)
a.sort()
for x in a: print(x, end = ' ')
