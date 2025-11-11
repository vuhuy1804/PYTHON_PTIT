n = int(input())
a, chan, le, d = [], [], [], [0] * n
while True:
    a.extend(list(map(int, input().split())))
    if len(a) == n: break
for i in range(n):
    if a[i] % 2 == 0:
        chan.append(a[i])
        d[i] = 1
    else:
        le.append(a[i])
le.sort()
chan.sort(key = lambda x : -x)
for i in range(n) :
    if d[i] == 1 :
        print(chan[-1], end = " ")
        chan.pop()
    else :
        print(le[-1], end = " ")
        le.pop()