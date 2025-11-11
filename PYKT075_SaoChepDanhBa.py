class Person:
    def __init__(self, ten, sdt, ngay):
        self.ten = ten
        self.sdt = sdt
        self.ngay = ngay
    
    def getName(self):
        a = self.ten.split()
        return a[-1] + ' ' + ' '.join(a[:-1])
    
    def out(self):
        return self.ten + ': ' + self.sdt + ' ' + self.ngay

def isName(s):
    for c in s:
        if c.isdigit(): return False
    return True

def isPN(s):
    for c in s:
        if c.isalpha(): return False
    return True

f1 = open("SOTAY.txt", "r")
f2 = open("DIENTHOAI.txt", "w")
a = []
ten, sdt, ngay = '', '', ''
for s in f1:
    s = s[:-1]
    if isName(s): ten = s
    elif isPN(s):
        sdt = s
        x = Person(ten, sdt, ngay)
        a.append(x)
    else: ngay = s[5:]
a.sort(key = lambda x : x.getName())
for x in a:
    f2.write(x.out() + '\n')
f1.close()
f2.close()