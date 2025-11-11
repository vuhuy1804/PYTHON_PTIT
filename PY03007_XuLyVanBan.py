a = []
while True:
    try:
        line = input().split()
        for i in range(len(line)):
            line[i] = line[i].lower()
        a.extend(line)
    except: break
a[0] = a[0][0].upper() + a[0][1:]
for i in range(len(a)):
    if a[i][-1] == '.' or a[i][-1] == '!' or a[i][-1] == '?':
        a[i] = a[i][:-1]
        print(a[i])
        if i != len(a) - 1:
            a[i + 1] = a[i + 1][0].upper() + a[i + 1][1:]
    else:
        print(a[i], end = ' ')