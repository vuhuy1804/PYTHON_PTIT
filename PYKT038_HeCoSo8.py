def DecToOct(n):
    if n < 8:
        print(n, end = '')
        return 
    DecToOct(n // 8)
    print(n % 8, end = '')

n = input()
res = 0
for i in n:
    res = res * 2 + (ord(i) - ord('0'))
DecToOct(res)