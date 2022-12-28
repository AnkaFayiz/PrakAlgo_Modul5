def banner():
    print("""
    ==== Program File Handling ====
    1. Membuat dan Menulis File
    2. Membaca File
    3. Menambahkan Text Pada File
    4. Keluar Dari Program
    """)

def membuat_dan_menulis():
    nama_file = input("Masukkan Nama File : ")
    nama = input("Masukkan Namamu : ")
    nim = int(input("Masukkan NIM kamu : "))
    tahun = int(input("Masukkan tahun angkatanmu : "))

    file = open(f"{nama_file}.txt", "w")
    file.write(f"Nama : {nama.capitalize()}\n")
    file.write(f"NIM : {nim}\n")
    file.write(f"Angkatan : {tahun}\n")
    
    # close file
    file.close()

def membaca_file():
    nama_file = input("Masukkan Nama File : ")
    file = open(f"{nama_file}.txt", "r")
    print(file.read())

    file.close()

def menambahkan():
    nama_file = input("Masukkan Nama File : ")
    file = open(f"{nama_file}.txt", "a")
    
    nama_sahabat = input("Masukkan Nama Sahabatmu : ")
    catatan_tambahan = input("Masukkan Catatan Tambahan kamu : ")

    file.write(f"Nama Sahabat : {nama_sahabat.capitalize()} \n")
    file.write(f"Catatan : {catatan_tambahan}\n")
    
if __name__ == '__main__':
    while True:
        banner()
        choice = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4) : "))
        if choice == 1:
            membuat_dan_menulis()
        elif choice == 2:
            membaca_file()
        elif choice == 3:
            menambahkan()
        elif choice == 4:
            exit()
        else:
            print("Nothing, Your input is error!")

