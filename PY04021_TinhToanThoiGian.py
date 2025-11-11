class Gamer:
    def __init__(self, id, ten, tgian):
        self.id = id
        self.ten = ten
        self.tgian = tgian
    
    def getTgian(self):
        return self.tgian
    
    def __str__(self):
        h = self.tgian // 60
        m = self.tgian % 60
        return f'{self.id} {self.ten} {str(h)} gio {str(m)} phut'
    
n = int(input())
a = []
for _ in range(n):
    id, ten, vao, ra = input(), input(), input(), input()
    h1, m1, h2, m2 = int(vao[:2]), int(vao[3:]), int(ra[:2]), int(ra[3:])
    tgian = (h2 * 60 + m2) - (h1 * 60 + m1)
    x = Gamer(id, ten, tgian)
    a.append(x)
a.sort(key = lambda x : -x.getTgian())
for x in a: print(x)