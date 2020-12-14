from django.db import models
import datetime


class Mortgage_values(models.Model):
    id = models.IntegerField(primary_key=True)
    source = models.CharField(max_length=20)
    year = models.IntegerField()
    created = models.DateField()
    down_payment_level = models.IntegerField()
    first_mortgage = models.BooleanField()
    long_amortization = models.BooleanField()
    rate_type = models.CharField(max_length=20)
    rate = models.DecimalField(max_digits=3, decimal_places=2)
    posted = models.BooleanField()
    type = models.CharField(max_length=20)

    objects = models.Manager()
