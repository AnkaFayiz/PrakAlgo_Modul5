def file_handling(name, age, addr, email, teacher):
    # Write File
    with open('Biodata.txt', 'w') as f:
        f.write(f'Name          : {name.capitalize()} \n')
        f.write(f'Age           : {age} \n')
        f.write(f'Address       : {addr.capitalize()} \n')
        f.write(f'Email         : {email} \n')
        f.write(f'Dosen Wali    : {teacher.capitalize()}')
        f.close()

    # Read file
    with open('Biodata.txt', 'r') as f:
        print("\nBerikut Data diri : ")
        print(f'{f.read()}')
        f.close()

if __name__ == '__main__':
    name = input("Masukkan Nama             : ")
    age = int(input("Masukkan Umur             : "))
    addr = input("Masukkan Alamat           : ")
    email = input("Masukkan Email            : ")
    teacher = input("Masukkan Dosen Walimu     : ")

    file_handling(name, age, addr, email, teacher)
