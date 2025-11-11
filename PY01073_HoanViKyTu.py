import itertools

s = input().strip()
for p in itertools.permutations(s):
    print(''.join(p))
