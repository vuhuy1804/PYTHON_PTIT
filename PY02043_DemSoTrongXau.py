t = int(input())
while t > 0:
    s = input()
    n = input()
    k = len(n)
    if n in s:
        cnt = 0
        while n in s:
            i = s.find(n)
            cnt += 1
            s = s[:i] + s[i+k:]
        print(cnt)
    else: print(0)
    t -= 1