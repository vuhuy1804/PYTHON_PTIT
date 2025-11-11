class ThiSinh:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    
    def getTongDiem(self):
        return self.d1 + self.d2 + self.d3

    def __str__(self):
        return f'{self.ten} {self.ns} {self.getTongDiem():.1f}'

if __name__ == '__main__':
    x = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
    print(x)