def check(n):
    if len(n) % 2 == 0: return False
    for i in range(2, len(n), 2):
        if n[i] != n[i-2]: return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')