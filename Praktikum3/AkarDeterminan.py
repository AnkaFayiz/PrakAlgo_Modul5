# Menghitung akar persamaan kuadrat dan determinan
import math 

if __name__ == '__main__':
    # Nilai persamaan 
    a = int(input("Nilai a : "))
    b = int(input("Nilai b : "))
    c = int(input("Nilai c : "))

    print(f'''
        Persamaan Kuadrat : 
        {a}x^2 + {b}x + {c} = 0
    ''')

    # Menghitung determinan dari persamaan kuadrat
    D = b**2 - 4*a*c 

    # Menghitung nilai persamaan x1 dan x2 
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2 / a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2 / a)

    print(f'''
        Persamaan Kuadrat : 
        {a}x^2 + {b}x + c = 0
    Hasil : 
        Diskriminan : 
        D = {D}
        Nilai X1 dan X2 : 
        X1 = {x1}
        X2 = {x2}
    ''') 
