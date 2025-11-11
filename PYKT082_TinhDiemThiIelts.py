def p(x):
    if x >= 39: return 9.0
    elif x >= 37: return 8.5
    elif x >= 35: return 8.0
    elif x >= 33: return 7.5
    elif x >= 30: return 7.0
    elif x >= 27: return 6.5
    elif x >= 23: return 6.0
    elif x >= 20: return 5.5
    elif x >= 16: return 5.0
    elif x >= 13: return 4.5
    elif x >= 10: return 4.0
    elif x >= 7: return 3.5
    elif x >= 5: return 3.0
    elif x >= 3: return 2.5
    return 1.0

t = int(input())
for _ in range(t):
    rea, lis, spea, wri = map(float, input().split())
    rea, lis = p(rea), p(lis)
    res = (rea + lis + spea + wri) / 4
    e = res - int(res)
    if e >= 0.75: res = int(res) + 1.0
    elif e >= 0.25: res = int(res) + 0.5
    else: res = float(int(res))
    print(res)
        