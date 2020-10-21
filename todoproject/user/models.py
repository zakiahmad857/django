from django.db import models
from django.utils import timezone

# Create your models here.


class Kategori(models.Model):
    kategori = models.CharField(max_length=40, verbose_name='Nama Kategori')

    def __str__(self):
         return self.kategori

class Judul(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=False, verbose_name='Kategori')
    judul = models.CharField(max_length=50, verbose_name='Judul')

    nama = models.CharField(max_length=100, blank=False, default='default', verbose_name='Nama File')
    jumlah = models.IntegerField(null=True, verbose_name='Jumlah Halaman')

    def __str__(self):
         return self.judul

    # def full_name(self):
    #     return '{} {}'.format(self.first_name, self.last_name)
    # def __str__(self):
    #     return self.full_name()



class Meta:
    model = Kategori
    fields = ("username",)
