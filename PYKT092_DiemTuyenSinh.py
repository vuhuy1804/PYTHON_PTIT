KV = [0, 1.5, 1, 0]

class ThiSinh:
    def __init__(self, id, ten, diem, dt, kv):
        self.id = id
        self.ten = ' '.join(ten.lower().split()).title()
        self.diem = diem
        self.dt = dt
        self.kv = kv

        self.diem += KV[int(kv)]
        if dt != 'Kinh': self.diem += 1.5
        self.kq = ('Do' if self.diem >= 20.5 else 'Truot')
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.diem} {self.kq}'

n = int(input())
a = []
for i in range(n):
    id = 'TS' + '{:02d}'.format(i + 1)
    a.append(ThiSinh(id, input(), float(input()), input(), input()))
a.sort(key = lambda x : -x.diem)
for x in a : print(x)