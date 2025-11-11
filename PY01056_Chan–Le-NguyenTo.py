from math import *

def prime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return n > 1

def check(n):
    sum = 0
    for i in range(len(n)):
        x = ord(n[i]) - ord('0')
        if (i % 2) != (x % 2):
            return False
        sum += x
    return prime(sum)

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')
