from django.db import models


# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return "%s the place " % self.name


class Restaurant(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    serve_hot_dog = models.BooleanField(default=False)
    serve_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant " % self.name


class Waiter(models.Model):
    name = models.CharField(max_length=20)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "%s the waiter " % self.name
