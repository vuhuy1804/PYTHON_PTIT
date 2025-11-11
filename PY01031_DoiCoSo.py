def DecConvert(n, b):
    if n < b:
        if (b > 10 and n >= 10):
            print(chr(ord('A') + n - 10), end = '')
        else: print(n, end = '')
        return 
    DecConvert(n // b, b)
    r = n % b
    if (b > 10 and r >= 10):
        print(chr(ord('A') + r - 10), end = '')
    else: print(r, end = '')
t = int(input())
for _ in range(t):
    n, b = map(int, input().split())
    DecConvert(n, b)
    print()