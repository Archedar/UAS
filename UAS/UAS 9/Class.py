#Class Mahasiswa
class Mahasiswa:
	def __init__(self, nama, kehadiran, tugas, uts, uas):
		self.nama = nama
		self.kehadiran = kehadiran
		self.tugas = tugas
		self.uts = uts
		self.uas = uas

	def cekKelulusan(self):
		if self.kehadiran >= 80 and self.tugas >= 80 and self.uts >= 85 and self.uas >= 75:
			print(f'{self.nama} Lulus')
		elif self.uts <= 79 and self.tugas <= 79:
			print(f'{self.nama} tidak lulus')
		elif self.uas <= 74:
			print(f'{self.nama} remidi')
		elif self.kehadiran <= 75:
			print(f'{self.nama} nilai D')