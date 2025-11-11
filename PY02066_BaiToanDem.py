n = int(input())
cnt = [0] * 1000001
a = []
while True:
    try: a.extend(map(int, input().split()))
    except: break
for x in a:
    cnt[x] += 1
ok = 1
r = max(a)
for i in range(1, r + 1):
    if cnt[i] == 0:
        ok = 0 
        print(i)
if ok == 1: print('Excellent!')