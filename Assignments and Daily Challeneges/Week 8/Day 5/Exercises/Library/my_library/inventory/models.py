from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    year = models.DateField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)