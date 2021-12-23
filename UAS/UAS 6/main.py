#Main Program
from Class import Kota

kota = [
	Kota('Jombang', 1),
	Kota('Surabaya', 2),
	Kota('Bandung', 3),
	Kota('Jakarta', 4)
]
cadangan = [
	Kota('Jombang', 1),
	Kota('Surabaya', 2),
	Kota('Bandung', 3),
	Kota('Jakarta', 4)
]
tersedia1, tersedia2= [
	1, 2, 3, 4, 5,
	6, 7, 8, 9, 10,
	11, 12, 13, 14, 15,
	16, 17, 18, 19, 20,
	21, 22, 23, 24, 25,
	26, 27, 28, 29, 30
],[
	1, 2, 3, 4, 5,
	6, 7, 8, 9, 10,
	11, 12, 13, 14, 15,
	16, 17, 18, 19, 20,
	21, 22, 23, 24, 25,
	26, 27, 28, 29, 30
]
terpakai1, terpakai2 = list(), list()

while True:
	print('\nAsal')
	for i in range(len(kota)):
		umpan = kota[i]
		print(f'{i + 1}. {umpan.nama}')
	asal = int(input('Pilih no kota asal: '))
	umpan1 = kota[asal - 1]
	del kota[asal - 1]
	print('\nTujuan')
	for i in range(len(kota)):
		umpan = kota[i]
		print(f'{i + 1}. {umpan.nama}')
	tujuan = int(input('Pilih no kota tujuan: '))
	umpan2 = kota[tujuan - 1]
	kota = cadangan.copy()
	pilihan = input('Apakah ingin memilih no kursi manual (y/n)? ')
	if pilihan == 'y':
		print(f'Gerbong 1')
		print(f'Gerbong 2')
		gerbong = int(input('Pilih Gerbong yang anda inginkan (1/2): '))
		if gerbong == 1:
			print(f'Gerbong 1, Kursi yang tersedia sebagai berikut\n{tersedia1}')
			kursi = int(input('Pilih no kursi yang diinginkan: '))
			del tersedia1[kursi - 1]
			terpakai1.append(kursi)
			jarak = umpan2.jarak - umpan1.jarak
			harga = 10000 * jarak
		elif gerbong == 2:
			print(f'Gerbong 2, Kursi yang tersedia sebagai berikut\n{tersedia2}')
			kursi = int(input('Pilih no kursi yang diinginkan: '))
			del tersedia2[kursi - 1]
			terpakai2.append(kursi)
			jarak = umpan2.jarak - umpan1.jarak
			harga = 10000 * jarak
	elif pilihan == 'n':
		if len(tersedia1) > 0:
			kursi = tersedia1[-1]
			del tersedia1[kursi - 1]
			terpakai1.append(kursi)
			jarak = umpan2.jarak - umpan1.jarak
			harga = 10000 * jarak
		elif len(tersedia2) == 0:
			kursi = tersedia1[-1]
			del tersedia2[kursi - 1]
			terpakai2.append(kursi)
			jarak = umpan2.jarak - umpan1.jarak
			harga = 10000 * jarak
	print('\nTiket')
	print(f'Asal {umpan1.nama} - Tujuan {umpan2.nama}\n Harga {harga}\n No Kursi: {kursi}')