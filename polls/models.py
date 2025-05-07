from django.db import models

# Create your models here.
class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    price = models.FloatField()
    decs = models.TextField()

    def __str__(self):
        return self.flavor
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    ice_cream = models.ManyToManyField(IceCream, related_name='brands')

    def __str__(self):
        return self.brand_name