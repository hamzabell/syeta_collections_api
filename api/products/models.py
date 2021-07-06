from django.db import models
from core.models  import Company

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)