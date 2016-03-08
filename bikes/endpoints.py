from rest_framework import generics

from .models import Bike
from .serializers import BikeSerializer, BikeSerpySerializer


class BikeListAPIView(generics.ListAPIView):
    queryset = Bike.objects.select_related('rider')
    #queryset = Bike.objects.all()
    serializer_class = BikeSerializer
