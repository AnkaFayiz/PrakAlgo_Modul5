class Mahasiswa:
    def __init__(self, name, NIM, angkatan):
        self.name = name
        self.NIM = NIM
        self.angkatan = angkatan

    def printBiodata(self):
        print(f'Nama        : {self.name}')
        print(f'NIM         : {self.NIM}')
        print(f'Angkatan    : {self.angkatan}')
    
if __name__ == '__main__':
    name = input("Masukkan Namamu : ")
    NIM = int(input("Masukkan NIM kamu : "))
    angkatan = int(input("Masukkan Tahun Angkatanmu : "))

    obj = Mahasiswa(name, NIM, angkatan)
    obj.printBiodata()
