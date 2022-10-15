print("Tiket Masuk Kebun Binatang!")
harga_total = 0

while True:
    umur = input("Masukkan umur : ")
    if umur != '':
        umur = int(umur)
        if umur <= 2 and umur > 0:
            print("Gratis")
            harga_total += 0
        elif umur >= 3 and umur <= 12:
            print(f"Harga : ${float(14):.2f}")
            harga_total += 14.00
        elif umur >= 65:
            print(f"Harga : ${float(18):.2f}")
            harga_total += 18.00
        else:
            print(f"Harga : ${float(23):.2f}")
            harga_total += 23.00 
        print(f"Harga Total : {harga_total}")
    else:
        break

uang = int(input("Masukkan jumlah uang : "))
if (uang - harga_total) < 0:
    print(f"Uang Kembalian : {float(uang - harga_total):.2f}")
    print("Uang anda kurang!")
else:
    print(f"Uang Kembalian : {float(uang - harga_total):.2f}")
