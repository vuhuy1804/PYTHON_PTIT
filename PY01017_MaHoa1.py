for _ in range(int(input())):
    s = input()
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]: cnt += 1
        else:
            print(cnt, s[i - 1], sep = '', end = '')
            cnt = 1
    if cnt > 0: print(cnt, s[-1], sep = '')