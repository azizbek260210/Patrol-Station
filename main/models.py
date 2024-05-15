from django.db import models
# from django.contrib.auth.models import User

class PetrolStation(models.Model):
    """Zapravka ma'lumotlari"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='petrol-station/', blank=True, null=True)
    location = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    closing_time = models.TimeField()
    opening_time = models.TimeField()

    def __str__(self):
        return self.name
    

class FuelType(models.Model):
    """Yoqilg'i turi"""
    fuels = [
        ('P', 'Petrol'),
        ('E', 'Electric'),
        ('G', 'Gas'),
    ]
    name = models.CharField(max_length=1, choices=fuels, unique=True)

    def __str__(self):
        return dict(self.fuels)[self.name]
    

class FuelPrice(models.Model):
    """Yoqilg'i narxi"""
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.fuel_type} - {self.unit_price}"
    

class Car(models.Model):
    """Zapravkaga kelgan mashina"""
    station = models.ForeignKey(PetrolStation, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=50)
    car_num = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"{self.car_type} {self.car_num}"
    

class CarFueling(models.Model):
    """Mashinaga qancha yoqilg'i quyilganligi va qancha pul to'langanligi haqida"""
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    type_fuel = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    limit = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    paid_money = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car.car_num} - {self.limit} birlik"
