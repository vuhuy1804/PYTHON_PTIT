for _ in range(int(input())):
    res = 1
    for i in input():
        n = ord(i) - ord('0')
        if n > 0: res *= n
    print(res)
