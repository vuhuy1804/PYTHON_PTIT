class MonThi:
    def __init__(self, id, ngay, gio, phong):
        self.id = id
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
    
    def getSortedDate(self):
        a = self.ngay.split('/')
        return a[2] + '/' + a[1] + '/' + a[0]

    def __str__(self):
        return f'{self.id} {self.ngay} {self.gio} {self.phong}'


f = open('CATHI.in', 'r')
n = int(f.readline())
i = 1
a = []
for _ in range(n):
    id = 'C' + '{:03d}'.format(i)
    i += 1
    a.append(MonThi(id, f.readline().strip(), f.readline().strip(), f.readline().strip()))
a.sort(key = lambda x : (x.getSortedDate(), x.gio))
for x in a: print(x)