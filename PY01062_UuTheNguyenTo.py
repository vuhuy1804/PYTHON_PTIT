from math import *

def prime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return n > 1

def check(n):
    cnt = 0
    for i in n:
        if i == '2' or i == '3' or i == '5' or i == '7': cnt += 1
    return cnt > len(n) - cnt and prime(len(n))

for _ in range(int(input())):
    n = input()
    print('YES' if check(n) else 'NO')