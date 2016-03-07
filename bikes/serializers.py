from rest_framework import serializers

from .models import Rider, Bike


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('name',)


class BikeSerializer(serializers.ModelSerializer):
    rider = RiderSerializer()

    class Meta:
        model = Bike
        fields = ('name', 'rider',)
