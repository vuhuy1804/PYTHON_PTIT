from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        res = sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return res
    
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
      
    def getArea(self):
        a = self.a.distance(self.b)
        b = self.a.distance(self.c)
        c = self.b.distance(self.c)
        if max(a, b, c) * 2 >= a + b + c:
            return 'INVALID'
        else:
            d = sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            return f'{d:.2f}'

if __name__ == '__main__':
    a = []
    t = int(input())
    for x in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for index in range(t):
        triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
        print(triagle.getArea())
        i += 6
