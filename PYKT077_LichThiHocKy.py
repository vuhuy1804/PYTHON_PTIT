class CaThi:
    def __init__(self, maCa, maMon, tenMon, ngay, gio, nhom):
        self.maCa = maCa
        self.maMon = maMon
        self.tenMon = tenMon
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom

    def getSortedDate(self):
        d, m, y = self.ngay.split('/')
        return y + '/' + m + '/' + d
    
    def __str__(self):
        return f'{self.maCa} {self.maMon} {self.tenMon} {self.ngay} {self.gio} {self.nhom}'

M = dict()
a = []
n, m = map(int, input().split())
for i in range(n):
    maMon, tenMon = input(), input()
    M[maMon] = tenMon
for i in range(m):
    maCa = 'T' + '{:03d}'.format(i + 1)
    maMon, ngay, gio, nhom = input().split()
    a.append(CaThi(maCa, maMon, M[maMon], ngay, gio, nhom))
a.sort(key = lambda x : (x.getSortedDate(), x.gio, x.maMon))
for x in a : print(x)