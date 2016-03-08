import requests
from rest_framework import generics, filters, renderers
from rest_framework.response import Response

from .models import Bikeway, BikewayCategory
from .serializers import BikewaySerializer, BikewayCategorySerializer, \
    BikewaySerpySerializer
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
        # Bikeway.objects.filter(name='12345').exists() and True
        # for bikeway in Bikeway.objects.all():
        #     pass
        # for bikeway in Bikeway.objects.all():
        #     pass
        # requests.get('https://api.github.com/').json()
        return response


class BikewayListAPIJSONView(BikewayListAPIView):
    renderer_classes = (renderers.JSONRenderer,)


class BikewayListSerpyAPIJSONView(BikewayListAPIJSONView):
    serializer_class = BikewaySerpySerializer


class BikewayListNoSerializerAPIJSONView(BikewayListAPIJSONView):

    def list(self, request, *args, **kwargs):
        data = []
        for bikeway in list(self.queryset.all()):
            datum = {}
            datum['id'] = bikeway.id
            datum['name'] = bikeway.name
            datum['location'] = bikeway.location
            datum['condition'] = bikeway.condition
            datum['length'] = bikeway.length
            datum['category'] = {
                'name': bikeway.category.name,
                'is_separated': bikeway.category.is_separated
            }
            data.append(datum)
        return Response(data)


class BikewayCategoryListAPIView(generics.ListAPIView):
    queryset = BikewayCategory.objects.all()
    serializer_class = BikewayCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BikewayCategoryFilterSet
