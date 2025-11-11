import sys
import math

input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_primes(N):
    return [i for i in range(2, N+1) if is_prime(i)]

def count_excluded(x, primes):
    res = 0
    m = len(primes)
    for mask in range(1, 1 << m):
        lcm_val = 1
        bits = 0
        for i in range(m):
            if (mask >> i) & 1:
                bits += 1
                lcm_val = lcm_val * primes[i] // math.gcd(lcm_val, primes[i])
                if lcm_val > x:
                    break
        else:
            if bits % 2 == 1:
                res += x // lcm_val
            else:
                res -= x // lcm_val
    return res

def solve(L, R, N):
    primes = get_primes(N)
    total = R - L + 1
    bad = count_excluded(R, primes) - count_excluded(L - 1, primes)
    return total - bad

# Main loop
while True:
    line = sys.stdin.readline()
    if not line or line.strip() == "-1":
        break
    L, R = map(int, line.strip().split())
    N = int(sys.stdin.readline())
    print(solve(L, R, N))
