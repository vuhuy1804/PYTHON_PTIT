for _ in range(int(input())):
    s, n = input(), input()
    cnt = 0
    while n in s:
        cnt += 1
        i = s.find(n)
        s = s[:i] + s[i+len(n):]
    print(cnt)