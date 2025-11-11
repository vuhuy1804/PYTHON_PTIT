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
    T = int(input())
    e = []
    while True:
        try: e.extend(map(int, input().split()))
        except: break
    I = 0
    for t in range(T):
        n, m = e[I], e[I + 1]
        I += 2
        a = []
        for i in range(n): a.append([0]*m)
        while len(e) - I < n*m: e.append(0)
        for i in range(n):
            for j in range(m): a[i][j] = e[I+j]
            I+=m
        matrix = Matrix(n, m, a)
        res = matrix.tich()
        for i in range(n):
            for j in range(n):
                print(res[i][j], end = ' ')
            print()

