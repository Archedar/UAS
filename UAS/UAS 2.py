#Alpro uas no 2
sembako = list()

jumlah = int(input('Jumlah data: '))

for i in range(jumlah):
	print(f'\nData ke-{i + 1}')
	nama = input('Nama: ')
	penghasilan = int(input('Penghasilan perbulan Rp '))
	rumah = input('Apakah rumah sudah berdinding bata?(y/n)  ')
	kartu = input('Apakah memiliki kartu kurang mampu dari desa? (y/n)')

	if penghasilan < 1000000 and rumah == 'n' and kartu == 'y':
		umpan = f'Selamat pada Bapak/Ibu {nama}, Anda mendapatkan bantuan sembako!'
		sembako.append(umpan)
	else:
		umpan = f'Maaf pada Bapak/Ibu {nama}, Anda belum memenuhi kriteria penerima bantuan sembako!'
		sembako.append(umpan)

print('')
for i in sembako:
	print(i)
