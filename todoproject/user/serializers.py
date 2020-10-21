# serializers.py
from rest_framework import serializers

from user.models import Judul

class JudulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judul
        fields = ('judul', 'kategori','nama','jumlah')

    kategori = serializers.SerializerMethodField('get_kategori_name')

    def get_kategori_name(self, obj):
        return obj.kategori.kategori
