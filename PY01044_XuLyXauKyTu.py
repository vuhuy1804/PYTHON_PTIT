s1 = set(input().lower().split())
s2 = set(input().lower().split())
giao = s1 & s2
hop = s1 | s2
hop = sorted(list(hop))
giao = sorted(list(giao))
for x in hop: print(x, end = ' ')
print()
for x in giao: print(x, end = ' ')