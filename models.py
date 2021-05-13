from django.db import models

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete.DO_NOTHNG)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    zipcode = models.CharField(max_length=200)
    price = models.IntegerField(max_length=200)
    bedrooms = models.IntegerField(max_length=200)
    bathrooms = models.DecimalField(max_length=2,decimal_places=1)
    garage = models.IntegerField(max_length=200)
    sqft = models.IntegerField(max_length=200)
    lot_size = models.DecimalField(max_length=2,decimal_places=1)