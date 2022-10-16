if __name__ == '__main__':
    n = int(input("Masukkan jumlah maksimal : "))
    for i in range(n, 0, -1):
        for j in range(i):
            print(i, end='')
        print('\r')
