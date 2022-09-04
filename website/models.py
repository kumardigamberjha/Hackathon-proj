from django.db import models

class DBModel(models.Model):
    date = models.DateField()
    price = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.FloatField(default=0)
    sqft_living = models.IntegerField(default=0)
    sqft_lot = models.IntegerField(default=0)
    floors = models.FloatField(default=0)
    waterfront = models.IntegerField(default=0)
    view = models.IntegerField(default=0)
    condition = models.IntegerField(default=0)
    sqft_above = models.IntegerField(default=0)
    sqft_basement = models.IntegerField(default=0)
    yr_built = models.IntegerField(default=0)
    yr_renovated = models.IntegerField(default=0)
    street = models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.price)