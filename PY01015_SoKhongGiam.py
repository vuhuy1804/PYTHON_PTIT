def check(s):
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]: return False
    return True

for _ in range(int(input())):
    print("YES" if check(input()) else "NO")