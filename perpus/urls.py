from django.urls import path
# from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('daftar-buku/', views.BukuListView.as_view(), name="daftar_buku"),
    path('daftar-anggota/', views.AnggotaListView.as_view(), name="daftar_anggota"),
    path('create-buku/', views.CreateBukuView.as_view(), name="create_buku"),
    path('edit-buku/<int:pk>/', views.EditBukuView.as_view(), name="edit_buku"),
    path('hapus-buku/<int:id_buku>/', views.hapus_buku, name="hapus_buku"),
    path('create-anggota/', views.CreateAnggotaView.as_view(), name="create_anggota"),
    path('edit-anggota/<int:pk>/', views.EditAnggotaView.as_view(), name="edit_anggota"),
    path('hapus-anggota/<int:id_anggota>/', views.hapus_anggota, name="hapus_anggota"),
    path('peminjaman-buku/', views.CreatePeminjamanView.as_view(), name="minjem"),
    path('pengembalian-buku/', views.CreatePengembalianView.as_view(), name="kembali"),
    path("history-peminjaman/", views.history_minjem, name="history_minjem"),
    path("history-pengembalian/", views.history_kembali, name="history_kembali"),
]