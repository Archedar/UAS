#Menu
from Class import Barang

def menu1(barang):
	print('')
	for i in range(len(barang)):
		umpan = barang[i]
		print(f'{i + 1}. {umpan.nama}, Stok Tersedia: {umpan.kuantitas}')

def menu2(barang, histori):
	print('')
	nama = input('Nama Barang: ')
	while True:
		try:
			harga = int(input(f'Harga {nama}: '))
			break
		except ValueError:
			print('Invalid Input!')
			continue
	while True:
		try:
			kuantitas = int(input(f'Stok {nama}: '))
			break
		except ValueError:
			print('Invalid Input!')
			continue
	tempHistori = f'Behasil menambahkan barang {nama}, harga Rp {harga}/unit stok={kuantitas}' 
	histori.append(tempHistori)
	barang.append(Barang(nama, harga, kuantitas))

def menu3(barang, histori):
	print('')
	for i in range(len(barang)):
		umpan = barang[i]
		print(f'{i + 1}. {umpan.nama}, Stok Tersedia: {umpan.kuantitas}')
	while True:
		try:
			tambah = int(input('Pilih No Barang yang Ingin Ditambah Stoknya: '))
			break
		except ValueError:
			print('Invalid Input!')
			continue
	umpan = barang[tambah - 1]
	while True:
		try:
			stok = int(input(f'Tambahkan Stok {umpan.nama}: '))
			break
		except ValueError:
			print('Invalid Input!')
			continue
	tempHistori = f'Berhasil menambahkan stok barang {umpan.nama} sebanyak {stok}'
	histori.append(tempHistori)
	umpan.kuantitas += stok

def menu4(barang, histori):
	print('')
	for i in range(len(barang)):
		umpan = barang[i]
		print(f'{i + 1}. {umpan.nama}')
	while True:
		try:
			hapus = int(input('Pilih No barang yang ingin dihapus: '))
			break
		except ValueError:
			print('Invalid Input!')
			continue
	umpan = barang[hapus - 1]
	tempHistori = f'Berhasil menghapus barang {umpan.nama}'
	histori.append(tempHistori)
	del barang[hapus - 1]

def menu5(barang):
	hasil = list()
	print('')
	while True:
		keyword = input('Keyword barang yang ingin dicari: ')
		if keyword == '':
			print('Anda tidak memasukan keyword apapun!')
			continue
		else:
			break
	for i in range(len(barang)):
		umpan = barang[i]
		if keyword in umpan.nama:
			random = f'{umpan.nama}, stok tersedia {umpan.kuantitas}, harga Rp {umpan.harga}/unit'
			hasil.append(random)
	print(str(len(hasil)) + ' Hasil ditemukan')
	for i in range(len(hasil)):
		print(f'{i + 1}. {hasil[i]}')

def menu6(barang, histori):
	totalPembayaran = 0
	struk = list()
	print('')
	while True:
		try:
			jumlah = int(input('Jumlah barang yang dibeli: '))
			break
		except ValueError:
			print('Invalid Input!')
			continue

	for i in range(len(barang)):
		umpan = barang[i]
		print(f'{i + 1}. {umpan.nama} stok tersedia {umpan.kuantitas}, harga Rp {umpan.harga}/unit')

	while jumlah > 0:
		while True:
			try:
				namaBarang = int(input('Masukan no barang: '))
				umpan = barang[namaBarang - 1]
				if umpan.kuantitas > 0:
					break
				else:
					print('Stok barang tidak tersedia!')
					continue
			except ValueError:
				print('Invalid Input!')
				continue
		while True:
			jumlahBarang = int(input('Kuantitas: '))
			if jumlahBarang > jumlah:
				print('Kuantitas barang yang anda masukan sudah melebihi jumlah barang belanjaan anda!')
				continue
			else:
				umpan.kuantitas -= jumlahBarang
				break
		tempStruk = f'{umpan.nama} {jumlahBarang}x{umpan.harga}'
		struk.append(tempStruk)
		tempHistori = f'Stok barang {umpan.nama} berkurang {jumlahBarang}'
		histori.append(tempHistori)
		for i in range(jumlahBarang):
			totalPembayaran += umpan.harga
		jumlah -= jumlahBarang

	while True:
		print('\nTotal Harga: Rp ' + str(totalPembayaran))
		while True:
			try:
				uang = int(input('Masukan Uang Rp '))
				break
			except ValueError:
				print('Invalid Input!')
				continue
		if uang < totalPembayaran:
			print('Uang kurang dari total harga pembayaran!')
			continue
		elif uang >= totalPembayaran:
			print('\n<===Struk Pembayaran===>')
			for i in range(len(struk)):
				print(f'{i + 1} {struk[i]}')
			print('\nTotal 		Rp ' + str(totalPembayaran))
			print('Uang 		Rp ' + str(uang))
			print(f'Kembalian 	Rp ' + str(uang - totalPembayaran))
			break

def menu7(histori):
	print('\n<===Log Histori===>\n')
	for i in histori:
		print(i)
