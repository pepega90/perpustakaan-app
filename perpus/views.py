from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect

from .authenticated import user_is_authenticated
from .models import Anggota, Buku, Peminjaman, Pengembalian
from .forms import EditBukuForm, EditAnggotaForm, BukuForm, AnggotaForm, PeminjamanForm, PengembalianForm
# Create your views here.
def home(req):
	if user_is_authenticated(req):
		return render(req, "home.html", {
			'total_anggota': Anggota.objects.all().count(),
			'total_buku': Buku.objects.all().count(),
			'total_pengembalian': Pengembalian.objects.all().count(),
			'total_peminjaman': Peminjaman.objects.all().count()})
	return HttpResponseRedirect(reverse('login'))

def history_minjem(req):
	if user_is_authenticated(req):
		list_minjem = Peminjaman.objects.all()
		paginator = Paginator(list_minjem, 4)
		page_number = req.GET.get('page')
		page_obj = paginator.get_page(page_number)
		if req.method == 'POST':
			if req.POST.get('cari_data'):
				start = req.POST.get('start')
				end = req.POST.get('end')
				list_minjem = Peminjaman.objects.filter(tgl_pinjam__gte=start, tgl_kembali__lte=end)
				paginator = Paginator(list_minjem, 4)
				page_number = req.GET.get('page')
				page_obj = paginator.get_page(page_number)
				return render(req, 'history_minjem.html', {'page_obj': page_obj})
		return render(req, 'history_minjem.html', {'page_obj': page_obj})
	return HttpResponseRedirect(reverse('login'))


def history_kembali(req):
	if user_is_authenticated(req):
		list_kembali = Pengembalian.objects.all()
		paginator = Paginator(list_kembali, 4)
		page_number = req.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(req, 'history_kembali.html', {'page_obj': page_obj})
	return HttpResponseRedirect(reverse('login'))

def hapus_anggota(req, id_anggota):
	if user_is_authenticated(req):
		if req.method == 'POST':
			deleted_anggota = get_object_or_404(Anggota, id=id_anggota)
			if deleted_anggota.foto:
				deleted_anggota.foto.delete()
			deleted_anggota.delete()
		return HttpResponseRedirect(reverse('daftar_anggota'))
	return HttpResponseRedirect(reverse('login'))

def hapus_buku(req, id_buku):
	if user_is_authenticated(req):
		if req.method == 'POST':
			deleted_buku = get_object_or_404(Buku, id=id_buku)
			if deleted_buku.foto_buku:
				deleted_buku.foto_buku.delete()
			deleted_buku.delete()
		return HttpResponseRedirect(reverse('daftar_buku'))
	return HttpResponseRedirect(reverse('login'))

class BukuListView(ListView):
	paginate_by = 4
	model = Buku
	template_name = 'buku.html'


class AnggotaListView(ListView):
	paginate_by = 4
	model = Anggota
	template_name = 'anggota.html'


class CreatePeminjamanView(CreateView):
	model = Peminjaman
	form_class = PeminjamanForm
	template_name = 'add_minjem.html'
	success_url = reverse_lazy('home')


class CreatePengembalianView(CreateView):
	model = Pengembalian
	form_class = PengembalianForm
	template_name = 'add_kembali.html'
	success_url = reverse_lazy('home')


class CreateBukuView(CreateView):
	model = Buku
	form_class = BukuForm
	template_name = 'add_buku.html'
	success_url = reverse_lazy('daftar_buku')


class CreateAnggotaView(CreateView):
	model = Anggota
	form_class = AnggotaForm
	template_name = 'add_anggota.html'
	success_url = reverse_lazy('daftar_anggota')

class EditAnggotaView(UpdateView):
	model = Anggota
	form_class = EditAnggotaForm
	template_name = 'edit_anggota.html'
	success_url = reverse_lazy('daftar_anggota')

	def post(self, request, pk):
		if 'hapus' in self.request.POST:
			del_old_img = get_object_or_404(Anggota, pk=pk)
			if del_old_img.foto:
				del_old_img.foto.delete()
		return super(EditAnggotaView, self).post(request, pk)


class EditBukuView(UpdateView):
	model = Buku
	form_class = EditBukuForm
	template_name = 'edit_buku.html'
	success_url = reverse_lazy('daftar_buku')

	def post(self, request, pk):
		if 'hapus' in self.request.POST:
			del_old_img = get_object_or_404(Buku, pk=pk)
			if del_old_img.foto_buku:
				del_old_img.foto_buku.delete()
		return super(EditBukuView, self).post(request, pk)