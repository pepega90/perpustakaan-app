from django.contrib import admin
from .models import Anggota, Buku, Peminjaman, Pengembalian 
# Register your models here.
admin.site.register(Anggota)
admin.site.register(Buku)
admin.site.register(Peminjaman)
admin.site.register(Pengembalian)
