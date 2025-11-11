for _ in range(int(input())):
    sum = 0
    for i in input(): sum += ord(i) - ord('0')
    print('YES' if (sum >= 10 and str(sum) == str(sum)[::-1]) else 'NO')
