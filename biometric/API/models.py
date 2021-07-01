from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=128, null=False)
    cheese = models.CharField(max_length=128)
    pastry = models.CharField(max_length=128)
    secret_ingredient = models.CharField(max_length=128)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

