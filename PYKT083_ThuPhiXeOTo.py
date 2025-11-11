def DonGia(loaiXe, soGhe):
    if loaiXe == 'Xe_con':
        if soGhe == '5': return 10000
        return 15000
    elif loaiXe == 'Xe_tai': return 20000
    elif loaiXe == 'Xe_khach':
        if soGhe == '29': return 50000
        return 70000

n = int(input())
d = dict({})
for _ in range(n):
    bienSo, loaiXe, soGhe, huong, ngay = input().split()
    if huong == 'IN':
        if ngay not in d:
            d[ngay] = DonGia(loaiXe, soGhe)
        else:
            d[ngay] += DonGia(loaiXe, soGhe)
for x, y in d.items():
    print(x, y, sep = ': ')
    