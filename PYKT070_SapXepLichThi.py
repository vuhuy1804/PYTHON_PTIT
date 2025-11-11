MT, CT = dict(), dict()
LT = []

class MonThi:
    def __init__(self, id, ten, ht):
        self.id = id
        self.ten = ten
        self.ht = ht

class CaThi:
    def __init__(self, id, ngay, gio, phong):
        self.id = id
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
    
    def getSortedDate(self):
        a = self.ngay.split('/')
        return a[2] + '/' + a[1] + '/' + a[0]
    
class LichThi:
    def __init__(self, idCa, idMon, idNhom, soSV):
        self.idCa = idCa
        self.idMon = idMon
        self.idNhom = idNhom
        self.soSV = soSV

    def __str__(self):
        return f'{CT[self.idCa].ngay} {CT[self.idCa].gio} {CT[self.idCa].phong} {MT[self.idMon].ten} {self.idNhom} {self.soSV}'

f = open('MONTHI.in', 'r')
n = int(f.readline())
for i in range(n):
    id, ten, ht = f.readline().strip(), f.readline().strip(), f.readline().strip()
    MT[id] = MonThi(id, ten, ht)
f.close()
f = open('CATHI.in', 'r')
n = int(f.readline())
for i in range(n):
    id = 'C' + '{:03d}'.format(i + 1)
    ngay, gio, phong = f.readline().strip(), f.readline().strip(), f.readline().strip()
    CT[id] = CaThi(id, ngay, gio, phong)
f.close()
f = open('LICHTHI.in', 'r')
n = int(f.readline())
for i in range(n):
    idCa, idMon, idNhom, soSV = f.readline().strip().split()
    LT.append(LichThi(idCa, idMon, idNhom, soSV))
LT.sort(key = lambda x : (CT[x.idCa].getSortedDate(), CT[x.idCa].gio, x.idCa))
for x in LT: print(x)
