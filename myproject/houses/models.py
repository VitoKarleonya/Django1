from django.db import models

class House(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    house_number = models.CharField(max_length=20)
    entrances = models.PositiveIntegerField(default=1)
    apartments_per_entrance = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.city}, {self.street} {self.house_number}'
