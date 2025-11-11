class TramDo:
    def __init__(self, id, ten, tongGio, luongMua):
        self.id = id
        self.ten = ten
        self.tongGio = tongGio
        self.luongMua = luongMua

    def getTB(self):
        return f'{self.luongMua / self.tongGio:.2f}'
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.getTB()}'

n = int(input())
d = dict()
cnt = 0
while n > 0:
    ten, bd, kt, luongMua = input(), input(), input(), int(input())
    h1, m1, h2, m2 = int(bd[:2]), int(bd[3:]), int(kt[:2]), int(kt[3:])
    gio = (h2 + m2 / 60) - (h1 + m1 / 60)
    if ten not in d:
        cnt += 1
        id = 'T0' + str(cnt)
        d[ten] = TramDo(id, ten, gio, luongMua)
    else:
        d[ten].tongGio += gio
        d[ten].luongMua += luongMua
    n -= 1
for x, y in d.items(): print(y)   
