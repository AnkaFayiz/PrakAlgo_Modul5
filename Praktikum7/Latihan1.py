def bilangan_prima(n):
	if n % 2 == 1:
		print(f'{n} adalah bilangan prima')
	else:
		print(f'{n} adalah bukan bilangan prima')

if __name__ == '__main__':
	print("Program menghitung bilangan prima")
	while True: 
		n = int(input("Masukkan bilangan : " ))
		
		if n != -1:
			bilangan_prima(n)
		else:
			exit(0)
