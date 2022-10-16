import math

a = int(input("Input bilangan A : "))
b = int(input("Input bilangan B : "))

# Jumlah 
print(f'Jumlah dari {a} + {b} : {a + b} ')
# Selisih
print(f'Selish dari {b} - {a} : {abs(b - a)}')
# Perkalian 
print(f'Perkalian dari {a} * {b} : {a * b}')
# Sisa pembagian 
print(f'Sisa pembagian dari {a} % {b} : {a % b}')
# Log(a)
print("Nilai log10 dari {} : {:.2f}".format(a, math.log10(a)))
# Pangkat
print(f'Nilai pangkat dari {a}**{b} : {a**b}')
