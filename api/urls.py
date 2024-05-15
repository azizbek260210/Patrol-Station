from django.urls import path
from .views import *

urlpatterns = [
    path('petrol-stations/', PetrolStationListCreate.as_view(), name='petrolstation-list-create'),
    path('petrol-stations/<int:pk>/', PetrolStationDetail.as_view(), name='petrolstation-detail'),
    path('fuel-types/', FuelTypeListCreate.as_view(), name='fueltype-list-create'),
    path('fuel-type/<int:pk>/', FuelTypeDetail.as_view(), name='fueltype-detail'),
    path('fuel-prices/', FuelPriceListCreate.as_view(), name='fuelprice-list-create'),
    path('fuel-price/<int:pk>/', FuelPriceDetail.as_view(), name='fuelprice-detail'),
    path('cars/', CarListCreate.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarDetail.as_view(), name='car-detail'),
    path('car-fueling/', CarFuelingListCreate.as_view(), name='CarFueling-list-create'),
    path('car-fueling/<int:pk>/', CarFuelingDetail.as_view(), name='CarFueling-detail'),
]