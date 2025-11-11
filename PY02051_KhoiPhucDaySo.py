n = int(input())
a = []
b = []
s = 0
for i in range(n):
    b.append(list(map(int, input().split())))
    a.append(sum(b[-1])) #a[i] = 3 * so_thu_i + sum_n-1_so_con_lai
    s += a[-1]
if n == 2:
    for i in a:
        print(int(i / 2), end = ' ')
else:
    s = int(s / 2 / (n - 1)) # tong n so 1->n
    for i in a:
        print(int((i - s) / (n - 2)), end = ' ')