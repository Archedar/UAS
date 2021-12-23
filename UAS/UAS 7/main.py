#Main Program
from Class import Item

wadah1, wadah2, wadah3 = [
	Item('    =    ', 1),
	Item('   ===   ', 2),
	Item('  =====  ', 3),
	Item(' ======= ', 4),
	Item('=========', 5)
],[
	Item('         ', 0),
	Item('         ', 0),
	Item('         ', 0),
	Item('         ', 0),
	Item('         ', 0)
],[
	Item('         ', 0),
	Item('         ', 0),
	Item('         ', 0),
	Item('         ', 0),
	Item('         ', 0)
]





benar = [
	Item('    =    ', 1),
	Item('   ===   ', 2),
	Item('  =====  ', 3),
	Item(' ======= ', 4),
	Item('=========', 5)
]
langkah = 0

while True:
	cek1 = wadah2[0]
	cek2 = wadah3[0]
	if cek1.posisi == 1 or cek2.posisi == 1:
		print(f'Anda berhasil menyelesaikan game simulasi tumpukan balok dalam {langkah} langkah')
		break
	for i in range(len(wadah1)):
		umpan1, umpan2, umpan3 = wadah1[i], wadah2[i], wadah3[i]
		print(f'|   {umpan1.isi}   {umpan2.isi}   {umpan3.isi}   |')
	print('|       1           2           3       |')
	input1 = input('\nPindahkan susunan diblok (pilih 1/2/3) ')
	input2 = input('Ke blok (pilih 1/2/3) ')





	if input1 == '1':
		for i in range(len(wadah1)):
			umpan1 = wadah1[i]
			if umpan1.posisi != 0:
				break
		if input2 == '1':
			print('Susunan tidak berubah!')
		elif input2 == '2':
			wadah2.reverse()
			for i in range(len(wadah2)):
				umpan2 = wadah2[i]
				if umpan2.isi == '         ':
					umpan2.isi = umpan1.isi
					umpan2.posisi = umpan1.posisi
					umpan1.isi = '         '
					umpan1.posisi = 0
					wadah2.reverse()
					langkah += 1
					break
				elif umpan2.isi == '         ' and umpan1.posisi < umpan2.posisi:
					umpan2.isi = umpan1.isi
					umpan2.posisi = umpan1.posisi
					umpan1.isi = '         '
					umpan1.posisi = 0
					wadah2.reverse()
					langkah += 1
					break
		elif input2 == '3':
			wadah3.reverse()
			for i in range(len(wadah2)):
				umpan3 = wadah3[i]
				if umpan3.isi == '         ':
					umpan3.isi = umpan1.isi
					umpan3.posisi = umpan1.posisi
					umpan1.isi = '         '
					umpan1.posisi = 0
					wadah3.reverse()
					langkah += 1
					break
				elif umpan3.isi == '         ' and umpan1.posisi < umpan3.posisi:
					umpan3.isi = umpan1.isi
					umpan3.posisi = umpan1.posisi
					umpan1.isi = '         '
					umpan1.posisi = 0
					wadah3.reverse()
					langkah += 1
					break





	elif input1 == '2':
		for i in range(len(wadah1)):
			umpan2 = wadah2[i]
			if umpan2.posisi != 0:
				break
		if input2 == '1':
			wadah1.reverse()
			for i in range(len(wadah1)):
				umpan1 = wadah1[i]
				if umpan1.isi == '         ':
					umpan1.isi = umpan2.isi
					umpan1.posisi = umpan2.posisi
					umpan2.isi = '         '
					umpan2.posisi = 0
					wadah1.reverse()
					langkah += 1
					break
				elif umpan1.isi == '         ' and umpan2.posisi < umpan1.posisi:
					umpan1.isi = umpan2.isi
					umpan1.posisi = umpan2.posisi
					umpan2.isi = '         '
					umpan2.posisi = 0
					wadah1.reverse()
					langkah += 1
					break
		elif input2 == '2':
			print('Susunan tidak berubah!')
		elif input2 == '3':
			wadah3.reverse()
			for i in range(len(wadah3)):
				umpan3 = wadah3[i]
				if umpan3.isi == '         ':
					umpan3.isi = umpan2.isi
					umpan3.posisi = umpan2.posisi
					umpan2.isi = '         '
					umpan2.posisi = 0
					wadah3.reverse()
					langkah += 1
					break
				elif umpan3.isi == '         ' and umpan2.posisi < umpan3.posisi:
					umpan3.isi = umpan2.isi
					umpan3.posisi = umpan2.posisi
					umpan2.isi = '         '
					umpan2.posisi = 0
					wadah3.reverse()
					langkah += 1
					break





	elif input1 == '3':
		for i in range(len(wadah3)):
			umpan3 = wadah3[i]
			if umpan3.posisi != 0:
				break
		if input2 == '1':
			wadah1.reverse()
			for i in range(len(wadah1)):
				umpan1 = wadah1[i]
				if umpan1.isi == '         ':
					umpan1.isi = umpan3.isi
					umpan1.posisi = umpan3.posisi
					umpan3.isi = '         '
					umpan3.posisi = 0
					wadah1.reverse()
					langkah += 1
					break
				elif umpan1.isi == '         ' and umpan3.posisi < umpan1.posisi:
					umpan1.isi = umpan3.isi
					umpan1.posisi = umpan3.posisi
					umpan3.isi = '         '
					umpan3.posisi = 0
					wadah1.reverse()
					langkah += 1
					break
		elif input2 == '2':
			wadah2.reverse()
			for i in range(len(wadah2)):
				umpan2 = wadah2[i]
				if umpan2.isi == '         ':
					umpan2.isi = umpan3.isi
					umpan2.posisi = umpan3.posisi
					umpan3.isi = '         '
					umpan3.posisi = 0
					wadah2.reverse()
					langkah += 1
					break
				elif umpan2.isi == '         ' and umpan3.posisi < umpan2.posisi:
					umpan2.isi = umpan3.isi
					umpan2.posisi = umpan3.posisi
					umpan3.isi = '         '
					umpan3.posisi = 0
					wadah2.reverse()
					langkah += 1
					break
		elif input2 == '3':
			print('Susunan tidak berubah!')
