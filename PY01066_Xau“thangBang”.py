def check(n):
    l, r = 1, len(n) - 2
    while l <= r:
        a, b = ord(n[l]) - ord(n[l-1]), ord(n[r]) - ord(n[r+1])
        if abs(a) != abs(b):
            return False
        l += 1
        r -= 1
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')