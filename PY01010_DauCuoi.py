for _ in range(int(input())):
    n = input()
    print("YES" if n[:2] == n[-2:] else "NO")