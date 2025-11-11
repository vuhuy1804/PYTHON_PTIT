f = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def xoay(s):
    sum = 0
    for c in s: sum += ord(c) - ord('A')
    t = ''
    for c in s: t += f[(ord(c) - ord('A') + sum) % 26]
    return t

for _ in range(int(input())):
    s = input()
    n = len(s)
    s1, s2 = s[:(n//2)], s[(n//2):]
    s1, s2 = xoay(s1), xoay(s2)
    res = ''
    for i in range(len(s1)):
        res += f[(ord(s1[i]) - ord('A') + ord(s2[i]) - ord('A')) % 26]
    print(res)