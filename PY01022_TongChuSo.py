n = input()
if len(n) <= 1: print(1)
else:
    cnt = 0
    while len(n) > 1:
        cnt += 1
        sum = 0
        for i in n: sum += ord(i) - ord('0')
        n = str(sum)
    print(cnt)