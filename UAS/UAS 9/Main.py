#Main program
from Class import Mahasiswa

mahasiswa = list()

jumlah = int(input('Jumlah Mahasiswa: '))

for i in range(jumlah):
	nama = input('Nama: ')
	kehadiran = int(input('Nilai Kehadiran: '))
	tugas = int(input('Nilai Tugas: '))
	uts = int(input('Nilai UTS: '))
	uas = int(input('Nilai UAS: '))
	mahasiswa.append(Mahasiswa(nama, kehadiran, tugas, uts, uas))

for i in range(len(mahasiswa)):
	umpan = mahasiswa[i]
	umpan.cekKelulusan()