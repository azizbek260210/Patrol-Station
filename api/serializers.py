from main.models import *
from rest_framework import serializers

class PetrolStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetrolStation
        fields = '__all__'


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'


class FuelPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelPrice
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarFuelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFueling
        fields = '__all__'
