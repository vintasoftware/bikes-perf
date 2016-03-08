from rest_framework import serializers
import serpy

from .models import Bikeway, BikewayCategory


class BikewayCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BikewayCategory
        fields = ('name', 'is_separated')


class BikewaySerializer(serializers.ModelSerializer):
    category = BikewayCategorySerializer()

    class Meta:
        model = Bikeway
        fields = ('id', 'name', 'location', 'condition', 'category',
                  'length')


class BikewayCategorySerpySerializer(serpy.Serializer):
    name = serpy.Field()
    is_separated = serpy.BoolField()


class BikewaySerpySerializer(serpy.Serializer):
    id = serpy.IntField()
    name = serpy.Field()
    location = serpy.Field()
    condition = serpy.Field()
    category = BikewayCategorySerpySerializer()
    length = serpy.IntField()
