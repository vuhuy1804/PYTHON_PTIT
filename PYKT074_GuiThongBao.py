t = int(input())
for _ in range(t):
    line = input()
    a = line.split()
    cnt = 0
    res = ''
    for x in a:
        if cnt + len(x) <= 100:
            cnt += len(x) + 1
            res += x + ' '
        else:
            break
    print(res)