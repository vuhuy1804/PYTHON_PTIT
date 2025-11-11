from math import *

class PhanSo:
    def __init__(self, t, m):
        self.t = t
        self.m = m

    def RutGon(self):
        uc = gcd(self.t, self.m)
        self.t //= uc
        self.m //= uc

    def __str__(self):
        return f'{self.t}/{self.m}'
    
if __name__ == '__main__':
    t, m = map(int, input().split())
    p = PhanSo(t, m)
    p.RutGon()
    print(p)