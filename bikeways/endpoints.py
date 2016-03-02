from rest_framework import generics, filters, renderers

from .models import Bikeway, BikewayCategory
from .serializers import BikewaySerializer, BikewayCategorySerializer
from .filtersets import BikewayFilterSet, BikewayCategoryFilterSet
from .filter_backends import LimitFilterBackend


class BikewayListAPIView(generics.ListAPIView):
    queryset = Bikeway.objects.all()
    serializer_class = BikewaySerializer
    filter_backends = (filters.DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter,
                       LimitFilterBackend)
    filter_class = BikewayFilterSet
    search_fields = ('name', 'category__name')
    ordering_fields = ('name', 'category__name',
                       'condition', 'length')
    ordering = ('length', 'name')

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        list(Bikeway.objects.all())
        list(Bikeway.objects.all())
        return response


class BikewayListAPIJSONView(BikewayListAPIView):
    renderer_classes = (renderers.JSONRenderer,)


class BikewayCategoryListAPIView(generics.ListAPIView):
    queryset = BikewayCategory.objects.all()
    serializer_class = BikewayCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BikewayCategoryFilterSet
