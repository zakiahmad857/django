
# Create your views here.

from . import urls
# views.py
from rest_framework import viewsets

from .serializers import JudulSerializer
from .models import Judul
from rest_framework import generics



class JudulViewSet(viewsets.ModelViewSet):
    queryset = Judul.objects.all().order_by('judul')
    serializer_class = JudulSerializer

class cobafilter(generics.ListAPIView):
    serializer_class = JudulSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        kategori = self.request.kategori
        return Judul.objects.filter(kategori=kategori)
