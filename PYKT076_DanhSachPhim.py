TL = dict()
P = []

class Phim:
    def __init__(self, id, theLoai, ngay, ten, soTap):
        self.id = id
        self. theLoai = theLoai
        self.ngay = ngay
        self.ten = ten
        self.soTap = soTap
    
    def getSortedDate(self):
        d, m, y = self.ngay.split('/')
        return y + '/' + m + '/' + d
    
    def __str__(self):
        return f'{self.id} {self.theLoai} {self.ngay} {self.ten} {str(self.soTap)}'
    
n, m = map(int, input().split())
for i in range(n):
    TL['TL{:03d}'.format(i + 1)] = input()
for i in range(m):
    id = 'P{:03d}'.format(i + 1)
    P.append(Phim(id, TL[input()], input(), input(), int(input())))
P.sort(key = lambda x : (x.getSortedDate(), x.ten, -x.soTap))
for x in P : print(x)

