t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    c1 = [0] * 256
    c2 = [0] * 256
    for c in s1: c1[ord(c)] += 1
    for c in s2: c2[ord(c)] += 1
    ok = True
    for j in range(256):
        if c1[j] != c2[j]:
            ok = False
            break
    print('Test ' + str(i + 1) + ': ', end = '')
    print('YES' if ok else 'NO')