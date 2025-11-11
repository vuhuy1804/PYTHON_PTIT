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
      
    def getPerimeter(self):
        c1 = self.a.distance(self.b)
        c2 = self.a.distance(self.c)
        c3 = self.b.distance(self.c)
        if max(c1, c2, c3) * 2 >= c1 + c2 + c3:
            return 'INVALID'
        else:
            return f'{(c1 + c2 + c3):.3f}'

if __name__ == '__main__':
    a = []
    t = int(input())
    for x in range(t):
        a += [float(i) for i in input().split()]
    i = 0
    for index in range(t):
        triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
        print(triagle.getPerimeter())
        i += 6
