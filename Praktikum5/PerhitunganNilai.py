rata_rata = 0
kategoriNilai = {
        'A':4.00,
        'A-':3.75,
        'B+':3.50,
        'B':3.00,
        'B-':2.75,
        'C+':2.50,
        'C':2.00,
        'C-':1.75,
        'D':1.50,
        'E':1.25
 }
matkul = int(input("Input nilai berapa mata kuliah : "))
for i in range(matkul):
    nilai = input("Masukkan nilai : ")
    print(kategoriNilai[nilai])

    rata_rata += kategoriNilai[nilai]

print(f'Nilai rata - rata dari {matkul} mata kuliah : {float(rata_rata/matkul)}')
