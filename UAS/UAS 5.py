#Alpro uas no 5
hasil = list()

while True:
	try:
		deret = int(input('Jumlah deret angka: '))
		break
	except ValueError:
		print('Error lol :v')
awal = int(input('Angka awal: '))
kelipatan = int(input('Kelipatan angka: '))

for i in range(deret):
	hasil.append(awal)
	awal += kelipatan
	
print(hasil)