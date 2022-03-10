from django.db import models

class Product(models.Model):
    name = models.CharField(unique=True, max_length=30)
    #weight in kg 
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    #price in Rs.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name