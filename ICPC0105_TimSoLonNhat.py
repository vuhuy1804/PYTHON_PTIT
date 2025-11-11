t = int(input())
for i in range(t):
    s, t = input(), ''
    for c in s:
        if c.isdigit(): t += c
        else: t += ' '
    a = t.split()
    ans = 0
    for x in a: ans = max(ans, int(x))
    print(ans)