def tang(n):
    for i in range(1, len(n)):
        if n[i] <= n[i - 1]: return False
    return True

def giam(n):
    for i in range(1, len(n)):
        if n[i] >= n[i - 1]: return False
    return True

for _ in range(int(input())):
    n = input()
    ok = False
    for i in range(len(n)):
        if tang(n[:i+1]) and giam(n[i:]):
            ok = True
            break
    print('YES' if ok and len(n) >= 3 else 'NO')