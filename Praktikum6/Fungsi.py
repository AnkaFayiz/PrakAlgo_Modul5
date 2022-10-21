def nilai():
    rata_rata = 0
    matkul = 0
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
    while True:
        nilai = input("Masukkan nilai : ")
        if nilai == '' and matkul == 0:
            return 0
        elif nilai == '':
            print(f'Nilai rata - rata dari {matkul} mata kuliah : {float(rata_rata/matkul)}')
            exit(0)
        else:
            print(kategoriNilai[nilai.upper()])
            matkul += 1
            rata_rata += kategoriNilai[nilai.upper()]

if __name__ == '__main__':
    nilai()
