while True:
    n = int(input())
    if n == 0: break
    s = set()
    while n != 1:
        s.add(n)
        if n % 2 == 0: n //= 2
        else: n = n*3 + 1
    print(len(s)+1)