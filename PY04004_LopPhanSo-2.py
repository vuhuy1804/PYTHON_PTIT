from math import *

class PhanSo:
    def __init__(self, t, m):
        self.t = t
        self.m = m
    
    def RutGon(self):
        uc = gcd(self.t, self.m)
        self.t //= uc
        self.m //= uc

    def cong(self, other):
        p = PhanSo(0, 0)
        bc = self.m // gcd(self.m, other.m) * other.m
        p.t = self.t * bc // self.m + other.t * bc // other.m
        p.m = bc
        p.RutGon()
        return p
    
    def __str__(self):
        return f'{self.t}/{self.m}'
    
if __name__ == '__main__':
    a = list(map(int, input().split()))
    p1, p2 = PhanSo(a[0], a[1]), PhanSo(a[2], a[3])
    p1.RutGon()
    p2.RutGon()
    print(p1.cong(p2))