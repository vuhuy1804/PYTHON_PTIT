diemUT = [0, 2.0, 1.5, 1.0, 0]
mon = ['TOAN', 'LY', 'HOA']
class GiaoVien:
    def __init__(self, id, ten, maXT, diemTH, diemCM):
        self.id = id
        self.ten = ten
        self.mon = mon[ord(maXT[0]) - ord('A')]
        self.tong = diemTH * 2 + diemCM + diemUT[int(maXT[1])]
        self.ketQua = ('TRUNG TUYEN' if self.tong >= 18 else 'LOAI')
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.mon} {self.tong:.1f} {self.ketQua}'
    
n = int(input())
a = []
for i in range(n):
    id = 'GV' + '{:02d}'.format(i + 1)
    a.append(GiaoVien(id, input(), input(), float(input()), float(input())))
a.sort(key = lambda x : -x.tong)
for x in a : print(x)