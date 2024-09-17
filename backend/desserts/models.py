from django.db import models

class DessertCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dessert(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(DessertCategory)
    price = models.FloatField()
    image = models.ImageField(upload_to="assets/images")

    def __str__(self):
        return self.name