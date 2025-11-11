def check(a, b):
    for i in range(1, len(a)):
        if abs(ord(a[i]) - ord(a[i-1])) != abs(ord(b[i]) - ord(b[i-1])): return False
    return True

for _ in range(int(input())):
    s = input()
    print("YES" if check(s, s[::-1]) else "NO")
