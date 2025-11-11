class KhachHang:
    def __init__(self, id, ten, tien):
        self.id = id
        self.ten = ten
        self.tien = tien
    
    def getTongTien(self):
        return self.tien

    def __str__(self):
        return f'{self.id} {self.ten} {str(self.tien)}'
    
def getTien(n):
    tien = 0
    if n <= 50: tien = 100 * n * 1.02
    elif n <= 100: tien = (100 * 50 + 150 * (n-50)) * 1.03
    else: tien = (100 * 50 + 150 * 50 + 200 * (n-100)) * 1.05
    return round(tien)
    

n = int(input())
a = []
for i in range(1, n + 1):
    ten, cu, moi = input(), int(input()), int(input())
    id = 'KH' + '{:02d}'.format(i)
    x = KhachHang(id, ten, getTien(moi - cu))
    a.append(x)
a.sort(key = lambda x : -x.getTongTien())
for x in a: print(x)
