from datetime import datetime

gia = [0, 25, 34, 50, 80]

class KhachHang:
    def __init__(self, id, ten, soP, ngayNhan, ngayTra, tienDV):
        self.id = id
        self.ten = ten
        self.soP = soP
        self.soN = str(datetime.strptime(ngayTra, '%d/%m/%Y') - datetime.strptime(ngayNhan, '%d/%m/%Y')).split()[0]
        if self.soN == '0:00:00' : self.soN = 1
        else: self.soN = int(self.soN) + 1
        self.tong = gia[int(self.soP[0])] * self.soN + tienDV
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.soP} {str(self.soN)} {str(self.tong)}'

n = int(input())
a = []
for i in range(n):
    id = 'KH' + '{:02d}'.format(i + 1)
    ten, soP, ngayNhan, ngayTra, tienDV = input().strip(), input().strip(), input().strip(), input().strip(), int(input())
    x = KhachHang(id, ten, soP, ngayNhan, ngayTra, tienDV)
    a.append(x)
a.sort(key = lambda x : -x.tong)
for x in a: print(x)
    
