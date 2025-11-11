t = int(input())
for i in range(t):
    s, t = input(), ''
    for c in s:
        if c.isdigit(): t += c
        else: t += ' '
    a = t.split()
    ans = 1e18
    for x in a: ans = min(ans, int(x))
    print(ans)