from django import forms
from .models import Buku, Anggota, Peminjaman, Pengembalian

class BukuForm(forms.ModelForm):
	class Meta:
		model = Buku
		fields = ('kode_buku', 'judul_buku', 'pengarang', 'klasifikasi', 'foto_buku')
		widgets = {
			'kode_buku': forms.NumberInput(attrs={'class': 'form-control'}),
			'judul_buku': forms.TextInput(attrs={'class': 'form-control'}),
			'pengarang': forms.TextInput(attrs={'class': 'form-control'}),
			'klasifikasi': forms.Textarea(attrs={'class': 'form-control'}),
			# 'foto_buku': forms.FileInput(attrs={'class': 'form-control'}),
		}


class AnggotaForm(forms.ModelForm):
	class Meta:
		model = Anggota
		fields = ('nim', 'nama', 'jenis_kelamin', 'kelas', 'foto')
		widgets = {
			'nim': forms.NumberInput(attrs={'class': 'form-control'}),
			'nama': forms.TextInput(attrs={'class': 'form-control'}),
			'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
			'kelas': forms.TextInput(attrs={'class': 'form-control'}),
			# 'foto_buku': forms.FileInput(attrs={'class': 'form-control'}),
		}


class PeminjamanForm(forms.ModelForm):
	class Meta:
		model = Peminjaman
		fields = ('no_transaksi', 'tgl_pinjam', 'tgl_kembali', 'orang', 'buku')
		widgets = {
			'no_transaksi': forms.NumberInput(attrs={'class': 'form-control'}),
			'tgl_pinjam': forms.TextInput(attrs={'class': 'form-control', 'type':'date'}),
			'tgl_kembali': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
			'orang': forms.Select(attrs={'class': 'form-control'}),
			# 'buku': forms.Select(attrs={'class': 'form-control', 'multiple': True}),
		}


class PengembalianForm(forms.ModelForm):
	class Meta: 
		model = Pengembalian
		fields = ('minjem_transaksi', 'is_denda', 'nominal_denda')
		widgets = {
			'minjem_transaksi': forms.Select(attrs={'class': 'form-control'}),
			'nominal_denda': forms.NumberInput(attrs={'class': 'form-control'}),
		}


class EditAnggotaForm(forms.ModelForm):
	class Meta:
		model = Anggota
		fields = ('nim', 'nama', 'jenis_kelamin', 'kelas', 'foto')
		widgets = {
			'nim': forms.NumberInput(attrs={'class': 'form-control'}),
			'nama': forms.TextInput(attrs={'class': 'form-control'}),
			'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
			'kelas': forms.TextInput(attrs={'class': 'form-control'}),
			# 'foto_buku': forms.FileInput(attrs={'class': 'form-control'}),
		}


class EditBukuForm(forms.ModelForm):
	class Meta:
		model = Buku
		fields = ('kode_buku', 'judul_buku', 'pengarang', 'klasifikasi', 'foto_buku')
		widgets = {
			'kode_buku': forms.NumberInput(attrs={'class': 'form-control'}),
			'judul_buku': forms.TextInput(attrs={'class': 'form-control'}),
			'pengarang': forms.TextInput(attrs={'class': 'form-control'}),
			'klasifikasi': forms.Textarea(attrs={'class': 'form-control'}),
			# 'foto_buku': forms.FileInput(attrs={'class': 'form-control'}),
		}