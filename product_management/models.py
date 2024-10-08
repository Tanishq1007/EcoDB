from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
