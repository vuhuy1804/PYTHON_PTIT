from math import *

def prime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return n > 1

for _ in range(int(input())):
    sum = 0
    for i in input(): sum += ord(i) - ord('0')
    print('YES' if prime(sum) else 'NO')
