for _ in range(int(input())):
    n = input()
    tong, tich = 0, 1
    f = False
    for i in range(len(n)):
        x = ord(n[i]) - ord('0')
        if i % 2 == 1: tong += x
        else:
            if x != 0:
                tich *= x
                f = True
    print(tich if f else 0, tong)