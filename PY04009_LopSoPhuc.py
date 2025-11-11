class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    
    def cong(self, other):
        thuc = self.thuc + other.thuc
        ao = self.ao + other.ao
        return SoPhuc(thuc, ao)
    
    def nhan(self, other):
        thuc = self.thuc * other.thuc - self.ao * other.ao
        ao = self.thuc * other.ao + self.ao * other.thuc
        return SoPhuc(thuc, ao)
    
    def __str__(self):
        if self.ao > 0:
            return f'{str(self.thuc)} + {str(self.ao)}i'
        elif self.ao < 0:
            return f'{str(self.thuc)} - {str(-self.ao)}i'
        else:
            return str(self.thuc)
    
t = int(input())
while t > 0:
    a, b, c, d = map(int, input().split())
    A, B = SoPhuc(a, b), SoPhuc(c, d)
    C = (A.cong(B)).nhan(A)
    D = A.cong(B).nhan(A.cong(B))
    print(C, end = '')
    print(', ', end = '')
    print(D)
    t -= 1