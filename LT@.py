def cek_tahun_kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

while True:
    bulan = int(input("Masukkan bulan (1-12, atau 0 untuk keluar): "))
    if bulan == 0:
        break

    tahun = int(input("Masukkan tahun: "))

    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        hari_dalam_bulan = 31
    elif bulan in [4, 6, 9, 11]:
        hari_dalam_bulan = 30
    elif bulan == 2:
        hari_dalam_bulan = 29 if cek_tahun_kabisat(tahun) else 28
    else:
        print("Bulan tidak valid.")
        continue

    print(f"{hari_dalam_bulan} hari dalam bulan {bulan}.")

print("Bye bye :3")
