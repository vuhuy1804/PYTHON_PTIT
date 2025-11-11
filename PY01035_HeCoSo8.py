n = input()
while len(n) % 3 != 0: n = '0' + n
for i in range(0, len(n), 3):
    res = 0
    for j in range(i, i + 3):
        res = res * 2 + int(n[j])
    print(res, end = '')