kota = ['surabaya', 'jombang', 'bandung', 'jakarta']

for i in range(len(kota)):
	print(f'{i + 1} {kota[i]}')

asal = int(input('dari mana(masukan no kota): '))
if asal == 1:
	print('kota terdekat jombang')
elif asal == 2:
	print('kota terdekat surabaya dan bandung')
elif asal == 3:
	print('kota terdekat jombang dan jakarta')
elif asal == 4:
	print('kota terdekat bandung')
