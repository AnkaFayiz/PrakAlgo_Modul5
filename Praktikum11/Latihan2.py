class Mahasiswa:

    def __init__(self):
        self.name = None
        self.nilai = None
    
    def banner(self):
        print("===== Program OOP =====")
        print("1. Mendeklarasikan Objek")
        print("2. Menampilkan Objek")
        print("3. Merubah Nilai Objek")
        print("4. Menghapus Objek")
        print("5. Keluar dari program")

    def run(self):
        while True:
            self.banner()

            choice = int(input("\nMasukkan Pilihan berupa angka (1/2/3/4/5): "))
            
            if choice == 1:
                self.deklarasikanObjek()
            elif choice == 2:
                self.tampil()
            elif choice == 3:
                self.ubah()
            elif choice == 4:
                self.hapus()
            elif choice == 5:
                self.keluar()
            else:
                print("Error!")
    
    def deklarasikanObjek(self):
        nama = input("Masukkan Namamu: ")
        nilai = int(input("Masukkan Nilaimu : "))

        self.name = nama
        self.nilai = nilai
        print("Data berhasil ditambahkan\n")
        
    def tampil(self):
        print(f'Nama    : {self.name}')
        print(f'Nilai   : {self.nilai}')
    
    def ubah(self):
        choice = input("Apa yang ingin diubah (Nama/Nilai): ")

        if choice.capitalize() == 'Nama':
            nama = input("Masukkan Nama : ") 
            self.name = nama
        elif choice.capitalize() == 'Nilai':
            nilai = int(input("Masukkan Nilai : "))
            self.nilai = nilai
        print("Data berhasil diubah!\n")

    def hapus(self):
        self.name = None
        self.nilai = None
        print('Data berhasil dihapus!\n')

    def keluar(self):
        print("Thank for using our apps!")
        exit()

if __name__ == '__main__':
    obj = Mahasiswa()
    obj.run()
