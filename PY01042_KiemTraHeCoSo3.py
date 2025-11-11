for _ in range(int(input())):
    n = input()
    ok = True
    for i in n:
        if i != '0' and i != '1' and i != '2':
            ok = False
            break
    print('YES' if ok else 'NO')