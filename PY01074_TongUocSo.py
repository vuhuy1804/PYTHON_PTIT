import sys
from array import array

data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    print(0)
    raise SystemExit

n = data[0]
a = data[1:1+n]

# M = giá trị tuyệt đối lớn nhất để sàng SPF
M = max((abs(x) for x in a), default=0)
if M < 2:
    print(0)
    raise SystemExit

# Sàng ước nguyên tố nhỏ nhất (SPF)
spf = array('I', [0]) * (M + 1)
for i in range(2, M + 1):
    if spf[i] == 0:
        spf[i] = i
        if i * i <= M:
            step = i
            start = i * i
            for j in range(start, M + 1, step):
                if spf[j] == 0:
                    spf[j] = i

# Tính tổng các ước nguyên tố (kể cả lặp) cho từng số và cộng lại
total = 0
for x in a:
    x = abs(x)
    while x > 1:
        p = spf[x]
        total += p
        x //= p

print(total)
