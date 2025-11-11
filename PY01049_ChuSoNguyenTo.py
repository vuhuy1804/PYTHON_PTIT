from math import *

def prime(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return n > 1

for _ in range(int(input())):
    n = input()
    d = [i for i in n if (i == '2' or i == '3' or i == '5' or i == '7')]
    #print(d)
    print('YES' if (prime(len(n)) and (len(d) > len(n) - len(d))) else 'NO')