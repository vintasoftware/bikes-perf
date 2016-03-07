from rest_framework import generics

from .models import Bike
from .serializers import BikeSerializer


class BikeListAPIView(generics.ListAPIView):
    queryset = Bike.objects.select_related('rider')
    serializer_class = BikeSerializer
