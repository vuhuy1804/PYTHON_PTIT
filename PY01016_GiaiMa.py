for _ in range(int(input())):
    s = input()
    for i in range(0, len(s), 2):
        cnt = int(s[i+1])
        while cnt > 0:
            print(s[i], end = '')
            cnt -= 1
    print()