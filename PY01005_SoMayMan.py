n = input()
cnt = 0
for i in n:
    if i == '4' or i == '7': cnt += 1
print("YES" if (cnt == 4 or cnt == 7) else "NO")