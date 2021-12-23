#Alpro uas no 8
papan = ['a', 'a', 'a', ' ', 'b', 'b', 'b']
benar = ['b', 'b', 'b', ' ', 'a', 'a', 'a']
langkah = 0

print('pindahkan posisi huruf \'a\' ke posisi huruf \'b\' sehingga menjadi susunan seperti ', benar)
print('dengan ketentuan hanya boleh mengambil satu langkah atau melangkahi satu huruf\n')
while True:
	while True:
		print('\nsusunan -> ', papan)
		print('index   ->  [ 0    1    2    3    4    5    6 ]\n')
		umpan1 = int(input('pilih index yang akan dipindah: '))
		umpan2 = int(input('pindahkan ke index: '))
		if umpan1 > umpan2:
			hasil = umpan1 - umpan2
			if (hasil == 1 or hasil == 2) and papan[umpan2] == ' ':
				papan.insert(umpan2, papan[umpan1])
				del papan[umpan2 + 1]
				papan.insert(umpan1, ' ')
				del papan[umpan1 + 1]
				langkah += 1
				break
			else:
				print('Langkah melanggar ketentuan!')
				continue 
		elif umpan1 < umpan2:
			hasil = umpan2 - umpan1
			if (hasil == 1 or hasil == 2) and papan[umpan2] == ' ':
				papan.insert(umpan2, papan[umpan1])
				del papan[umpan2 + 1]
				papan.insert(umpan1, ' ')
				del papan[umpan1 + 1]
				langkah += 1
				break
			else:
				print('Langkah melanggar ketentuan!')
				continue
		elif umpan1 == umpan2:
			print('Posisi susunan tidak berubah')
			continue
	if papan == benar:
		break
print(f'Anda telah memenangkan permainan menukar tempat dengan {langkah} langkah')