def find(n, k):
    x = 2 ** (n - 1)
    if k == x: return n
    if k > x: return find(n - 1, k - x)
    else: return find(n - 1, k)

t = int(input())
while t > 0:
    n, k = map(int, input().split())
    print(chr(ord('A') + find(n, k) - 1))
    t -= 1