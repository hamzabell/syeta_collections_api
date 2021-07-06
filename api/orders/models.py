from django.db import models
from core.models import Company

STATUS_CHOICES = (
    ('ACTIVE', 'Active'),
    ('EXPIRED', 'Expired'),
    ('SUSPENDED', 'Suspended')
)
# Create your models here.
class Discount(models.Model):
    code = models.CharField(max_length=255)
    percentage = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, default='ACTIVE', max_length=10)
    expiryDate = models.DateTimeField()
    company =models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    discount_code = models.ManyToManyField(Discount)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    company =models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
