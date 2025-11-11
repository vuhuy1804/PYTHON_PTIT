class ThiSinh:
    def __init__(self, id, ten, diemTB):
        self.id = id
        self.ten = ten
        self.diemTB = diemTB
    
    def getDiemTB(self):
        return self.diemTB
    
    def getKQ(self):
        x = self.diemTB
        if x < 5: return 'TRUOT'
        elif x < 8: return 'CAN NHAC'
        elif x <= 9.5: return 'DAT'
        else: return 'XUAT SAC'
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.diemTB:.2f} {self.getKQ()}'
    
n = int(input())
a = []
for i in range(1, n + 1):
    id = 'TS0' + str(i)
    ten = input()
    d1, d2 = float(input()), float(input())
    if d1 > 10: d1 /= 10
    if d2 > 10: d2 /= 10
    diemTB = (d1 + d2) / 2
    x = ThiSinh(id, ten, diemTB)
    a.append(x)
a.sort(key = lambda x : -x.getDiemTB())
for x in a: print(x)