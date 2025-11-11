class SinhVien:
    def __init__(self, id, ten, lop, cc):
        self.id = id
        self.ten = ten
        self.lop = lop
        self.cc = cc
    
    def output(self):
        print(self.id, self.ten, self.lop, self.cc, end = ' ')
        print('KDDK' if self.cc == 0 else ' ')

n = int(input())
d = dict()
for _ in range(n):
    id, ten, lop = input(), input(), input()
    x = SinhVien(id, ten, lop, 10)
    d[id] = x
for _ in range(n):
    id, dd = input().split()
    cc = 10
    for c in dd:
        if c == 'm': cc -= 1
        elif c == 'v': cc -= 2
    if cc < 0: cc = 0
    d[id].cc = cc
for x, y in d.items(): y.output()