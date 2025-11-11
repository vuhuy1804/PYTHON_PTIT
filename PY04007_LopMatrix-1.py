class Matrix:
    def __init__(self, n, m, x):
        self.n = n
        self.m = m
        self.x = x
    
    def tich(self):
        n, m = self.n, self.m
        a = self.x
        b = [[0 for _ in range(n)] for _ in range(m)]
        c = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                b[j][i] = a[i][j]
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            a.append(list(map(int, input().split())))
        matrix = Matrix(n, m, a)
        res = matrix.tich()
        for i in range(n):
            for j in range(n):
                print(res[i][j], end = ' ')
            print()
        t -= 1

