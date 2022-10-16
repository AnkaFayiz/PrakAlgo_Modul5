print("Hitung Luas Ruangan")
panjang = int(input("Masukkan Panjang Ruangan: "))
lebar = int(input("Masukkan Lebar Ruangan: "))
satuan = input("Masukkan Satuan (Meter/Inci): ")

if satuan.capitalize() == 'Meter':
    print(f'Luas ruangan dengan panjang {float(panjang)} dan lebar {float(lebar)} adalah {float(panjang*lebar)} Meter')
elif satuan.capitalize() == 'Inci':
    result = '{:.2f}'.format(panjang*lebar*39.37)
    print(f'Luas ruangan dengan panjang {float(panjang*39.37)} dan lebar {float(lebar*39.37)} adalah {float(result)} Inci')
else:
    print("Error! Pilihan anda tidak ada di menu ")
