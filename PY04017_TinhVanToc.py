class ThiSinh:
    def __init__(self, id, ten, donVi, vanToc, tgian):
        self.id = id
        self.ten = ten
        self.donVi = donVi
        self.vanToc = vanToc
        self.tgian = tgian
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.donVi} {str(self.vanToc)} Km/h'
    
n = int(input())
a = []
for i in range(n):
    ten, donVi, tgDich = input(), input(), input()
    id = ''
    for s in donVi.split(): id += s[0]
    for s in ten.split(): id += s[0]
    tgian = (int(tgDich[:-3]) * 60 + int(tgDich[-2:]) - 6 * 60) / 60
    vanToc = round(120 / tgian)
    x = ThiSinh(id, ten, donVi, vanToc, tgian)
    a.append(x)
a.sort(key = lambda x : x.tgian)
for x in a: print(x)
    