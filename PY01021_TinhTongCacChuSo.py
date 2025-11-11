t = int(input())
for _ in range(t):
    s = input()
    res = sum([int(c) for c in s if c.isdigit()])
    a = [c for c in s if c.isalpha()]
    a.sort()
    for c in a:
        print(c, end = '')
    print(res)