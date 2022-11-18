def rekursif():
    print("Ini merupakan program negatif dan positif, tekan enter untuk berhenti")
    angka = input("Masukkan Angka : ")
    if angka == '':
        print("Program Selesai")
        exit()

    pangkat = input("Masukkan Pangkat : ")

    print(f'Hasilnya adalah : {pow(int(angka), int(pangkat))}\n')

    rekursif()

rekursif()
