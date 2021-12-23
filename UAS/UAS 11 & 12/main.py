#Main Program
from Class import Barang
import Menu

histori = list()
listBarang = [
Barang('Rinso', 5000, 20),
Barang('Sabun', 3000, 20),
Barang('Pulpen', 2500, 20),
Barang('Tisu', 10000, 20),
Barang('Penggaris', 1000, 20)
]

while True:
	print('''
Menu
	1. Tampilkan Barang
	2. Tambahkan Barang
	3. Tambah Stock Barang
	4. Hapus Barang
	5. Cari Barang Berdasarkan Keyword
	6. Hitung Barang Belanjaan
	7. Histori Keluar Masuk Barang
	0. Keluar Program
		''')

	choice = input('Masukan No Menu: ')

	if choice == '1':
		Menu.menu1(listBarang)
	elif choice == '2':
		Menu.menu2(listBarang, histori)
	elif choice == '3':
		Menu.menu3(listBarang, histori)
	elif choice == '4':
		Menu.menu4(listBarang, histori)
	elif choice == '5':
		Menu.menu5(listBarang)
	elif choice == '6':
		Menu.menu6(listBarang, histori)
	elif choice == '7':
		Menu.menu7(histori)
	elif choice == '0':
		print('Keluar Program')
		break
	else:
		print('Invalid Input!')