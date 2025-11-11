def check(s):
    sum = ord(s[0]) - ord('0')
    for i in range(1, len(s)):
        sum += ord(s[i]) - ord('0')
        if abs(ord(s[i]) - ord(s[i-1])) != 2: return False
    return sum % 10 == 0

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')