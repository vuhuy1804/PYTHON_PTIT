from math import *

for _ in range(int(input())):
    n = input()
    print('YES' if gcd(int(n), int(n[::-1])) == 1 else 'NO')