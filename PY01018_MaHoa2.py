def inx(x):
    return(P.index(x))
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    a = input().split()
    if len(a) == 1: break
    k, s = int(a[0]), a[1]
    res = ''
    for i in range(len(s)):
        res += P[(inx(s[i]) + k) % 28]
    res = res[::-1]
    print(res)    
