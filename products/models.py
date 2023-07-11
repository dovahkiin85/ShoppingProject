from pyexpat import model
from django.db import models

class Products(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.IntegerField()
    p_desc = models.CharField(max_length=300)
    p_category = models.CharField(max_length=20)
    p_owner = models.CharField(max_length=100)
    p_available = models.BooleanField(default=True)
    p_stock = models.IntegerField()
