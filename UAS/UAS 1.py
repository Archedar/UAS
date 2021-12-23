#Alpro uas no 1
listNama = list()
acc = list()
umpan = 0

jumlah = int(input('Jumlah data: '))

for i in range(jumlah):
	listNama.append(input(f'Masukan Nama ke-{i + 1}: '))

for nama in listNama:
	for huruf in nama:
		if huruf in 'Aa':
			umpan += 1
		if umpan >= 3:
			acc.append(nama)
			umpan = 0
			break
		

print('\nList Nama Yang Diinput')
for i in listNama:
	print(i)
print('\nList Nama yang Mengandung Huruf Vokal "A/a" Lebih Dari 3')
for i in acc:
	print(i)
