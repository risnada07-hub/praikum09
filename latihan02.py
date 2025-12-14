nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah = 0

for n in nilai:
    try:
        total += n
        jumlah += 1
    except TypeError:
        # Melewati data yang bukan angka
        continue

if jumlah > 0:
    rata_rata = total / jumlah
    print("Rata-rata nilai valid:", rata_rata)
else:
    print("Tidak ada data nilai yang valid.")
