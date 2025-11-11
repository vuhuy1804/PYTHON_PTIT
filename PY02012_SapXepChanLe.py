n = int(input())
a = []
while True:
    try: a.extend(list(map(int, input().split())))
    except: break
chan, le = [], []
d = [0] * n
for i in range(n):
    if a[i] % 2 == 0:
        chan.append(a[i])
    else:
        le.append(a[i])
        d[i] = 1
chan.sort(reverse=True)
le.sort()
for i in range(n):
    if d[i] == 0:
        print(chan[-1], end = ' ')
        chan.pop()
    else:
        print(le[-1], end = ' ')
        le.pop()