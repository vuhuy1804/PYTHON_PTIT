def check(s):
    dotCount = 0
    for c in s:
        if c == '.': dotCount += 1
        elif c.isdigit() == False:
            return False
    if dotCount != 3:
        return False
    a = list(map(int, s.split('.')))
    if len(a) != 4:
        return False
    for x in a:
        if x < 0 or x > 255:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    print('YES' if check(s) else 'NO')