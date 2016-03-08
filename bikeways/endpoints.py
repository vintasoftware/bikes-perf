import requests
from rest_framework import generics, filters, renderers
from rest_framework.response import Response

from .models import Bikeway, BikewayCategory
from .serializers import BikewaySerializer, BikewayCategorySerializer, \
    BikewaySerpySerializer
from .filtersets import BikewayFilterSet, BikewayCategoryFilterSet
from .filter_backends import LimitFilterBackend


class BikewayListAPIView(generics.ListAPIView):
    queryset = Bikeway.objects.select_related('category')
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


from rest_framework.negotiation import BaseContentNegotiation


class IgnoreClientContentNegotiation(BaseContentNegotiation):
    def select_parser(self, request, parsers):
        """
        Select the first parser in the `.parser_classes` list.
        """
        return parsers[0]

    def select_renderer(self, request, renderers, format_suffix):
        """
        Select the first renderer in the `.renderer_classes` list.
        """
        return (renderers[0], renderers[0].media_type)


class BikewayListSlimAPIView(BikewayListAPIView):
    permission_classes = []
    authentication_classes = []
    filter_backends = []
    renderer_classes = [renderers.JSONRenderer]
    content_negotiation_class = IgnoreClientContentNegotiation
