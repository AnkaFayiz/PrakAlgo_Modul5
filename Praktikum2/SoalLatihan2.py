import math 

# Kota 1 
print("Kota 1")
lat_1 = float(input("Masukkan nilai latitude kota 1 : "))
long_1 = float(input("Masukkan nilai longtitude kota 1 : "))

# Kota 2
print("\nKota 2")
lat_2 = float(input("Masukkan nilai latitude kota 2 : "))
long_2 = float(input("Masukkan nilai longtitude kota 2 : "))

dlat = lat_2 - lat_1
dlong = long_2 - long_1

# Rumus trigonometri 
trigono = math.sin(math.radians(dlat/2)) ** 2 + math.cos(math.radians(lat_1)) * math.cos(math.radians(lat_2)) * math.sin(math.radians(dlong/2)) ** 2

# Arc Sinus
arc_sinus = math.asin(math.sqrt(trigono))

# Arc Tangen
R = 6371.01

print("Jarak antar kedua titik Kota 1 dengan Kota 2 adalah {:.2f} kilometer".format(arc_sinus * R))
