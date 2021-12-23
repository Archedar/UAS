#Main Program
from Class import Orang

kandidat = list()

def isi():
	jumlah = int(input('Jumlah data: '))
	for i in range(jumlah):
		print(f'Data ke-{i + 1}')
		nama = input('Nama: ')
		pendapatan = int(input('Pendapatan: '))
		rumah = input('Apakah rumah sudah terbangun dari batu bata (y/n): ')
		kartu = input('Apakah punya kartu bantuan dari desa (y/n): ')
		kandidat.append(Orang(nama, pendapatan, rumah, kartu))

isi()

while True:
	print('\nMain Menu:\n1. Tampilkan semua data\n2. Tampilkan penerima sembako\n3. Tampilkan yang tidak menerima sembako\n4. Tambahkan data\n5. Keluar program')

	choice = input('Masukan no menu: ')

	if choice == '1':
		print('')
		for i in kandidat:
			i.semua()
	elif choice == '2':
		print('')
		for i in kandidat:
			i.dapat()
	elif choice == '3':
		print('')
		for i in kandidat:
			i.tidakDapat()
	elif choice == '4':
		print('')
		isi()
	elif choice == '5':
		break
	else:
		print('Invalid Input!')