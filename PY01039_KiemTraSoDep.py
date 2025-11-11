def check(n):
    for i in range(1,len(n)):
        if n[i]==n[i-1] or (i>1 and n[i]!=n[i-2]): return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')
