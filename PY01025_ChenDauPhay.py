s, t = input(), ''
cnt = 0
for i in range(len(s) - 1, -1, -1):
    t += s[i]
    cnt += 1
    if cnt % 3 == 0 and i != 0: t += ','
print(t[::-1])