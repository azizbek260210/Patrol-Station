from rest_framework import generics
from main.models import *
from .serializers import *


class PetrolStationListCreate(generics.ListCreateAPIView):
    queryset = PetrolStation.objects.all()
    serializer_class = PetrolStationSerializer


class PetrolStationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetrolStation.objects.all()
    serializer_class = PetrolStationSerializer


class FuelTypeListCreate(generics.ListCreateAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class FuelTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer


class FuelPriceListCreate(generics.ListCreateAPIView):
    queryset = FuelPrice.objects.all()
    serializer_class = FuelPriceSerializer


class FuelPriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FuelPrice.objects.all()
    serializer_class = FuelPriceSerializer


class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarFuelingListCreate(generics.ListCreateAPIView):
    queryset = CarFueling.objects.all()
    serializer_class = CarFuelingSerializer


class CarFuelingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarFueling.objects.all()
    serializer_class = CarFuelingSerializer