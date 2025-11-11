from math import *

def prime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return n > 1

def check(n):
    for i in range(len(n)):
        if prime(i) != prime(ord(n[i]) - ord('0')):
            return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')
