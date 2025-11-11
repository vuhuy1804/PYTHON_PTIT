from math import ceil

class SinhVien:
    def __init__(self, id, ten, d1, d2, d3):
        self.id = id
        self.ten = ' '.join(ten.lower().split()).title()
        self.d = (d1 * 3 + d2 * 3 + d3 * 2) / 8

    def __str__(self):
        return f'{self.id} {self.ten} {ceil(self.d * 100) / 100:.2f} {str(self.rank)}'
    
n = int(input())
a = []
for i in range(n):
    id = 'SV{:02d}'.format(i + 1)
    a.append(SinhVien(id, input(), int(input()), int(input()), int(input())))
a.sort(key = lambda x : -x.d)
a[0].rank = 1
for i in range(1, len(a)):
    a[i].rank = a[i-1].rank if a[i].d == a[i-1].d else i + 1
for x in a: print(x)


