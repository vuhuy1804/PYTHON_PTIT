def xoay(s):
    t = s[1:] + s[0]
    return t

def solve(a, n):
    ans = 10**9
    for i in range(n):
        res = 0
        for j in range(n):
            if a[i] == a[j]: continue
            tmp = a[j]
            cnt = 0
            while(tmp != a[i]):
                tmp = xoay(tmp)
                cnt += 1
                if cnt > len(tmp):
                    return -1
            res += cnt
        ans = min(ans, res)
    return ans

n = int(input())
a = [input() for _ in range(n)]
print(solve(a, n))