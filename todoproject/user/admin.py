from django.contrib import admin
from .models import Kategori, Judul


@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    pass

@admin.register(Judul)
class JudulAdmin(admin.ModelAdmin):
    list_display = ["judul", "kategori", "jumlah"]


# Register your models here.
