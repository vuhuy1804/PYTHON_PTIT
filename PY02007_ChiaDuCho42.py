a = []
while True:
    try: a.extend(map(int, input().split()))
    except: break
s = set([x % 42 for x in a])
print(len(s))