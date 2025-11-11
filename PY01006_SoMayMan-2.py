for _ in range(int(input())):
    n = input()
    ok = True
    for i in n:
        if i != '4' and i != '7':
            ok = False
            break
    print("YES" if ok else "NO")