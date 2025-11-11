n = int(input())
a = list(map(float, input().split()))
minn, maxx = min(a), max(a)
b = [x for x in a if (x != minn and x != maxx)]
res = sum(b) / len(b)
print('%.2f' % res)