f = open('CONTACT.in', 'r')
s = set()
for x in f:
    x = x.strip().lower()
    s.add(x)
a = sorted(list(s))
for x in a: print(x)