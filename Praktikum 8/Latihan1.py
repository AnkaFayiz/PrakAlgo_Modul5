def rekursif(n, angka = 1):
    inputUser = int(input(f'Masukkan bilangan ke-{angka} : '))
    inputUser += inputUser
    if angka == n:
        print(f'Hasil dari Penjumlahan : {inputUser} ')
        exit()

    rekursif(n, angka + 1)


if __name__ == '__main__':
    n = int(input("Masukkan Jumlah : "))
    rekursif(n)
