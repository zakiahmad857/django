from rest_framework.generics import ListAPIView

from user.serializers import JudulSerializer
from user.models import Judul

class JudulList(ListAPIView):
    queryset = Judul.objects.all()
    serializer_class = JudulSerializer
