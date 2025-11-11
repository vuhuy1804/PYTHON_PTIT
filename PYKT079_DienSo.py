t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_val, min_val = max(a), min(a)
    s = set(a)
    print(max_val - min_val + 1 - len(s))