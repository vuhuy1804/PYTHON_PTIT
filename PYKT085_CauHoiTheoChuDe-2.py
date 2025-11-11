a = []
n = int(input())
for _ in range(n):
    a.append(input())
while len(a) > 0:
    idx = len(a)
    for i in range(len(a)):
        if a[i] == '':
            idx = i
            break
    print(a[0], ': ', idx - 1, sep = '')
    a = a[idx + 1:]