for _ in range(int(input())):
    sum = 0
    for i in input(): sum += ord(i) - ord('0')
    print('YES' if sum % 3 == 0 else 'NO')
