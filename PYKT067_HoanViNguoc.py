from itertools import *

for _ in range(int(input())):
    n = int(input())
    a = [x for x in range(1, n + 1)]
    res = list(permutations(a))
    res = res[::-1]
    print(len(res))
    for x in res:
        for i in x: print(i, end = '')
        print(' ', end = '')
    print()