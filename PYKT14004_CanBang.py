from itertools import combinations

a = []
while True:
    try:
        a.extend(map(int, input().split()))
    except:
        break

res = 10**18
n = 12
people = list(range(n))

for g1 in combinations(people[1:], 2):
    gr1 = {0, *g1}
    rem1 = [x for x in people if x not in gr1]
    for g2 in combinations(rem1, 3):
        gr2 = set(g2)
        rem2 = [x for x in rem1 if x not in gr2]
        for g3 in combinations(rem2, 3):
            gr3 = set(g3)
            gr4 = [x for x in rem2 if x not in gr3]

            sums = [
                sum(a[i] for i in gr1),
                sum(a[i] for i in gr2),
                sum(a[i] for i in gr3),
                sum(a[i] for i in gr4),
            ]
            res = min(res, max(sums) - min(sums))

print(res)
