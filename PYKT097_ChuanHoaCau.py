a = []
while True:
    try: a.append(input())
    except: break

for s in a:
    s = ' '.join(s.split()).capitalize()
    if s[-1].isalpha() or s[-1].isdigit(): s += '.'
    if s[-2] == ' ': s = s[:-2] + s[-1]
    print(s)
