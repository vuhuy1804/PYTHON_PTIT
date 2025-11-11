class MatHang:
    def __init__(self, id, ten, sl, donGia, chietKhau):
        self.id = id
        self.ten = ten
        self.sl = sl
        self.donGia = donGia
        self.chietKhau = chietKhau
        self.tong = sl * donGia - chietKhau

    def __str__(self):
        return f'{self.id} {self.ten} {str(self.sl)} {str(self.donGia)} {str(self.chietKhau)} {str(self.tong)}'
    
n = int(input())
a = []
for i in range(n):
    a.append(MatHang(input(), input(), int(input()), int(input()), int(input())))
a.sort(key = lambda x : -x.tong)
for x in a : print(x)