for _ in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        res = 1
        for j in range(1, int(i)+1): res *= j
        sum += res
    print('Yes' if int(n) == sum else 'No')