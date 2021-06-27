from django.db import models
from datetime import date

kelamin_list = (
	("L", "Laki-laki"),
	("P", "Perempuan"),
)

# Create your models here.
class Anggota(models.Model):
	nim = models.IntegerField()
	nama = models.CharField(max_length=255)
	jenis_kelamin = models.CharField(max_length=255, choices=kelamin_list)
	kelas = models.CharField(max_length=255)
	foto = models.ImageField(null=True, blank=True, upload_to="images/orang")

	def __str__(self):
		return self.nama

class Buku(models.Model):
	kode_buku = models.IntegerField()
	judul_buku = models.CharField(max_length=255)
	pengarang = models.CharField(max_length=255)
	klasifikasi = models.TextField(max_length=255)
	foto_buku = models.ImageField(null=True, blank=True, upload_to="images/buku")

	def __str__(self):
		return "%s - %s" % (self.judul_buku, self.pengarang)

class Peminjaman(models.Model):
	no_transaksi = models.IntegerField()
	tgl_pinjam = models.DateField()
	tgl_kembali = models.DateField()
	orang = models.OneToOneField(Anggota, on_delete=models.CASCADE)
	buku = models.ManyToManyField(Buku, related_name='buku_pinjam')

	def __str__(self):
		return f"{str(self.no_transaksi)} - Peminjam {self.orang.nama}"

class Pengembalian(models.Model):
	minjem_transaksi = models.OneToOneField(Peminjaman, on_delete=models.CASCADE)
	is_denda = models.BooleanField(default=False)
	nominal_denda = models.IntegerField(null=True,blank=True)

	def __str__(self):
		return f"Tgl Kembali {str(self.minjem_transaksi.tgl_kembali)} no transaksi {str(self.minjem_transaksi.no_transaksi)}"