class HocSinh:
    def __init__(self, id, ten, d):
        self.id = id
        self.ten = ten
        self.d = d

    def getTB(self):
        diem = sum(self.d[:2]) * 2 + sum(self.d[2:])
        return round(diem / 12 + 1e-8, 1)
    
    def getKQ(self):
        diem = self.getTB()
        if diem >= 9: return 'XUAT SAC'
        elif diem >= 8: return 'GIOI'
        elif diem >= 7: return 'KHA'
        elif diem >= 5: return 'TB'
        else: return 'YEU'

    def __str__(self):
        return f'{self.id} {self.ten} {self.getTB():.1f} {self.getKQ()}'
    
n = int(input())
a = []
for i in range(1, n + 1):
    id = ''
    ten = input()
    d = list(map(float, input().split()))
    if i < 10: id = 'HS0' + str(i)
    else: id = 'HS' + str(i)
    x = HocSinh(id, ten, d)
    #print(x.getTB())
    a.append(x)
a.sort(key = lambda x : -x.getTB())
for x in a: print(x)
