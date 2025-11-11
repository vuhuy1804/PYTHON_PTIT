n = int(input())
d = dict({})
for _ in range(n):
    ten = input()
    c, t = map(int, input().split())
    d[ten] = [c, t]
a = list(d.items())
a.sort(key = lambda x : (-x[1][0], x[1][1], x[0]))
for x, y in a:
    print(x, y[0], y[1])