for _ in range(int(input())):
    n = input()
    cnt = 0
    while int(n) % 7 != 0 and cnt < 1000:
        n = str(int(n) + int(n[::-1]))
        cnt += 1
    print(n if cnt < 1000 else -1)