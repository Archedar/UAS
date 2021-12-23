#Main Program
#Alpro uas no 10
from Class import Kuis

listSoal = [
'1 + 1 = ',
'3 x 3 = ',
'25 : 5 = '
]

kuis = [
Kuis(listSoal[0], '2'),
Kuis(listSoal[1], '9'),
Kuis(listSoal[2], '5')
]

def mulaiKuis(kuis):
	skor = 0
	for i in kuis:
		jawaban = input(i.soal)
		if jawaban == i.jawaban:
			skor += 1
	print(f'Anda berhasil menjawab {skor} soal dengan benar dari {len(listSoal)} soal')

mulaiKuis(kuis)