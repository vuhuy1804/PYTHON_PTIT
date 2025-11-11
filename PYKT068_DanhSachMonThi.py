class MonHoc:
    def __init__(self, id, ten, hinhThuc):
        self.id = id
        self.ten = ten
        self.hinhThuc = hinhThuc
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.hinhThuc}'
    
n = int(input())
a = []
for i in range(n):
    a.append(MonHoc(input(), input(), input()))
a.sort(key = lambda x : x.id)
for x in a : print(x)