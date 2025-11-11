M = [100, 500, 200]

class KhachHang:
    def __init__(self, id, ten, loai, dau, cuoi):
        self.id = 'KH{:02d}'.format(id + 1)
        self.ten = ' '.join(ten.lower().split()).title()
        soDien = cuoi - dau
        DM = M[ord(loai) - ord('A')]
        if soDien <= DM:
            self.trongDM = soDien * 450
            self.ngoaiDM = 0
        else:
            self.trongDM = DM * 450
            self.ngoaiDM = (soDien - DM) * 1000
        self.vat = self.ngoaiDM // 20
        self.tong = self.trongDM + self.ngoaiDM + self.vat
    
    def __str__(self):
        return f'{self.id} {self.ten} {str(self.trongDM)} {str(self.ngoaiDM)} {str(self.vat)} {str(self.tong)}'
    
n = int(input())
KH = []
for i in range(n):
    ten = input()
    loai, dau, cuoi = input().split()
    KH.append(KhachHang(i, ten, loai, int(dau), int(cuoi)))
KH.sort(key = lambda x : -x.tong)
for x in KH : print(x)