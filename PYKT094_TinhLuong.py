P = dict()
H = [[10, 12, 14, 20], [10, 11, 13, 16], [9, 10, 12, 14], [8, 9, 11, 13]]

def bac(id):
    i = ord(id[0]) - ord('A')
    nam = int(id[1:])
    if nam <= 3: return H[i][0]
    elif nam <= 8: return H[i][1]
    elif nam <= 15: return H[i][2]
    return H[i][3]

class NhanVien:
    def __init__(self, id, ten, lcb, nc):
        self.id = id
        self.ten = ten
        self.phong = P[id[3:]]
        self.luong = lcb * nc * bac(id[:3]) * 1000
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.phong} {str(self.luong)}'
    
n = int(input())
for i in range(n):
    l = input().split()
    P[l[0]] = ' '.join(l[1:])
m = int(input())
NV = []
for i in range(m):
    NV.append(NhanVien(input(), input(), int(input()), int(input())))
for x in NV : print(x)