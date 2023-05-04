from django.db import models

PAYMENT = (
    ('gcash','GCash'),
    ('creditcard', 'Credit Card'),
)

class MyModel(models.Model):
  payment = models.CharField(max_length=6, choices=COLOR_CHOICES, default='gcash')

# Create your models here.
