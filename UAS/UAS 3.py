#Alpro uas no 3
data = list()

jumlah = int(input('Jumlah kalimat: '))

for i in range(jumlah):
	data.append(input(f'Masukan kalimat ke-{i + 1}: '))

while True:
	print('''
Menu
	1. Tampilkan semua data kalimat
	2. Cari
	3. Hapus semua data kalimat dan mengisi ulang data kalimat
 	4. Keluar program
''')

	pilihan = input('Masukan menu: ')

	if pilihan == '1':
		print('list semua data kalimat')
		for i in range(len(data)):
			print(f'{i + 1}. {data[i]}')
	elif pilihan == '2':
		hasil = list()
		keyword = input('Masukan keyword data kalimat yang ingin dicari: ')
		for kalimat in data:
			if keyword in kalimat:
				hasil.append(kalimat)
		print(f'{len(hasil)} hasil ditemukan untuk keyword \'{keyword}\'')
		for i in range(len(hasil)):
			print(f'{i + 1}. {hasil[i]}')
	elif pilihan == '3':
		data.clear()
		jumlah = int(input('Jumlah kalimat: '))

		for i in range(jumlah):
			data.append(input(f'Masukan kalimat ke-{i + 1}: '))
	elif pilihan == '4':
		print('Have a nice day')
		break