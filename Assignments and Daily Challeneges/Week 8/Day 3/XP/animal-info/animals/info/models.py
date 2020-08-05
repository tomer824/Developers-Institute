from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length = 100)

class Animals(models.Model):
    name = models.CharField(max_length = 100, default = 'null')
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)


