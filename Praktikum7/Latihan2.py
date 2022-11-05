def ordinal_num(number):
    if number == 1:
        print(f"({number}, 'st')")
    elif number == 2:
        print(f"({number}, 'nd')")
    elif number == 3:
        print(f"({number}, 'rd')")
    else:
        print(f"({number}, 'th')")

if __name__ == '__main__':
    print("Ordinal Number Program!")
    print("Ketik 0 untuk menghetikan program!")
    while True:
        number = int(input("Masukkan Angka : "))

        if number != 0:
            ordinal_num(number)
        else:
            print("Terima kasih telah menggunakan program!")
            exit(0)
