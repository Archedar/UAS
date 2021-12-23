#Class
class Orang:
	def __init__(self, nama, pendapatan, rumah, kartu):
		self.nama = nama
		self.pendapatan = pendapatan
		self.rumah = rumah
		self.kartu = kartu

	def dapat(self):
		if self.pendapatan < 1000000 and self.rumah == 'n' and self.kartu == 'y':
			print(f'{self.nama} Selamat anda memenuhi kriteria penerima bantuan sembako')

	def tidakDapat(self):
		if self.pendapatan >= 1000000 or self.rumah == 'y' or self.kartu == 'n':
			print(f'{self.nama} Mohon maaf anda belum memnuhi kriteria penerima bantuan sembako')

	def semua(self):
		if self.pendapatan < 1000000 and self.rumah == 'n' and self.kartu == 'y':
			print(f'{self.nama} Selamat anda memenuhi kriteria penerima bantuan sembako')
		else:
			print(f'{self.nama} Mohon maaf anda belum memnuhi kriteria penerima bantuan sembako')