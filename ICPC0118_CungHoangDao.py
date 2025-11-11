def solve(d, m):
    if m == 1:
        if d >= 20: return 'Bao Binh'
        return 'Ma Ket'
    if m == 2:
        if d >= 19: return 'Song Ngu'
        return 'Bao Binh'
    if m == 3:
        if d >= 21: return 'Bach Duong'
        return 'Song Ngu'
    if m == 4:
        if d >= 20: return 'Kim Nguu'
        return 'Bach Duong'
    if m == 5:
        if d >= 21: return 'Song Tu'
        return 'Kim Nguu'
    if m == 6:
        if d >= 21: return 'Cu Giai'
        return 'Song Tu'
    if m == 7:
        if d >= 23: return 'Su Tu'
        return 'Cu Giai'
    if m == 8:
        if d >= 23: return 'Xu Nu'
        return 'Su Tu'
    if m == 9:
        if d >= 23: return 'Thien Binh'
        return 'Xu Nu'
    if m == 10:
        if d >= 23: return 'Thien Yet'
        return 'Thien Binh'
    if m == 11:
        if d >= 23: return 'Nhan Ma'
        return 'Thien Yet'
    if m == 12:
        if d >= 22: return 'Ma Ket'
        return 'Nhan Ma'


for _ in range(int(input())):
    d, m = map(int, input().split())
    print(solve(d, m))