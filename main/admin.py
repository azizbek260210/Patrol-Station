from django.contrib import admin
from . import models

admin.site.register(models.PetrolStation)
admin.site.register(models.FuelType)
admin.site.register(models.FuelPrice)
admin.site.register(models.Car)
admin.site.register(models.CarFueling)
