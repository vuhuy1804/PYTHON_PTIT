s = input()
while len(s) > 1:
    i = len(s) // 2
    s1, s2 = int(s[:i]), int(s[i:])
    s = str(s1 + s2)
    print(s)
