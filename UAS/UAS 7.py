#Alpro uas no 7
wadah1, wadah2, wadah3, benar = [
	1, 2, 3, 4, 5
], [
	' ', ' ', ' ', ' ', ' '
], [
	' ', ' ', ' ', ' ', ' '
], [
	1, 2, 3, 4, 5
]
langkah = 0

while True:
	print('')
	for i in range(len(wadah1)):
		print(f'|{wadah1[i]}     {wadah2[i]}     {wadah3[i]}|')
	print(' a     b     c ')
	input1 = input('Pindahkan angka paling atas di-blok (pilih a/b/c) ')
	input2 = input('ke blok (pilih a/b/c) ')

	if input1 == 'a':
		for x in range(len(wadah1)):
			umpan1 = wadah1[x]
			if umpan1 != ' ':
				if input2 == 'a':
					print('Tumpukan tidak berubah!')
					break
				elif input2 == 'b':
					wadah2.reverse()
					for y in range(len(wadah2)):
						umpan2 = wadah2[y]
						if y == 0 and umpan2 == ' ':
							wadah2.insert(y, umpan1)
							del wadah2[y + 1]
							wadah1.insert(x, ' ')
							del wadah1[x + 1]
							wadah2.reverse()
							break
						elif umpan2 == ' ' and (umpan1 > wadah2[y - 1]):
							wadah2.insert(y, umpan1)
							del wadah2[y + 1]
							wadah1.insert(x, ' ')
							del wadah1[x + 1]
							wadah2.reverse()
							break
						else:
							print('Langkah melanggar ketentuan!')
							wadah2.reverse()
				elif input2 == 'c':
					wadah3.reverse()
					for y in range(len(wadah3)):
						umpan2 = wadah3[y]
						if y == 0 and umpan2 == ' ':
							wadah3.insert(y, umpan1)
							del wadah3[y + 1]
							wadah1.insert(x, ' ')
							del wadah1[x + 1]
							wadah3.reverse()
							break
						elif umpan2 == ' ' and (umpan1 > wadah3[y - 1]):
							wadah3.insert(y, umpan1)
							del wadah3[y + 1]
							wadah1.insert(x, ' ')
							del wadah1[x + 1]
							wadah3.reverse()
							break
						else:
							print('Langkah melanggar ketentuan!')
							wadah3.reverse()
				break

	elif input1 == 'b':
		for x in range(len(wadah2)):
			umpan1 = wadah2[x]
			if umpan1 != ' ':
				if input2 == 'a':
					wadah1.reverse()
					for y in range(len(wadah1)):
						umpan2 = wadah1[y]
						try:
							if y == 0 and umpan2 == ' ':
								wadah1.insert(y, umpan1)
								del wadah1[y + 1]
								wadah2.insert(x, ' ')
								del wadah2[x + 1]
								wadah1.reverse()
								break
							elif umpan1 < wadah1[y]:
								wadah1.insert(y, umpan1)
								del wadah2[y + 1]
								wadah2.insert(x, ' ')
								del wadah1[x + 1]
								wadah1.reverse()
								break
							else:
								print(wadah1[y - 1])
								print('Langkah melanggar ketentuan!')
								wadah1.reverse()
						except:
							wadah1.reverse()
							continue
				elif input2 == 'b':
					print('Tumpukan tidak berubah!')
					break
				elif input2 == 'c':
					wadah3.reverse()
					for y in range(len(wadah3)):
						umpan2 = wadah3[y]
						if y == 0 and umpan2 == ' ':
							wadah3.insert(y, umpan1)
							del wadah3[y + 1]
							wadah1.insert(x, ' ')
							del wadah1[x + 1]
							wadah3.reverse()
							break
						elif umpan2 == ' ' and (umpan1 > wadah3[y - 1]):
							wadah3.insert(y, umpan1)
							del wadah3[y + 1]
							wadah1.insert(x, ' ')
							del wadah1[x + 1]
							wadah3.reverse()
							break
						else:
							print('Langkah melanggar ketentuan!')
							wadah3.reverse()
				break

	elif input1 == 'c':
		pass
	else:
		print('Invalid Input!')
	if wadah2 == benar or wadah3 == benar:
		break

print('Anda telah menyelesaikan permainan tumpukan angka dalam {langkah} langkah')
