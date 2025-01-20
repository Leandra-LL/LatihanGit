def cari_terbesar(a, b, c):
    if a > b:
        terbesar = a
    else:
        terbesar = b
    if c > terbesar:
        terbesar = c
    return terbesar

print(cari_terbesar(10, 25, 15)) 



