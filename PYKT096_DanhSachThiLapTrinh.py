T = dict()

class ThiSinh:
    def __init__(self, id, ten, idTeam):
        self.id = 'C{:03d}'.format(id + 1)
        self.ten = ten
        self.tenTeam = T[idTeam][0]
        self.tenTruong = T[idTeam][1]
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.tenTeam} {self.tenTruong}'
    
n = int(input())
for i in range(n):
    idTeam = 'Team{:02d}'.format(i + 1)
    tenTeam, tenTruong = input(), input()
    T[idTeam] = [tenTeam, tenTruong]
m = int(input())
TS = []
for i in range(m):
    TS.append(ThiSinh(i, input(), input()))
TS.sort(key = lambda x : x.ten)
for x in TS : print(x)