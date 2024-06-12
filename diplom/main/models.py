
from django.db import models
from django.utils import timezone


class Services(models.Model):
    UTILITY_CHOICES = [
        ('gas', 'газ'),
        ('svet', 'свет'),
        ('voda', 'вода'),
    ]

    account_number = models.CharField(max_length=100)
    tariff = models.DecimalField(max_digits=6, decimal_places=2)
    meter_reading = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    utility_type = models.CharField(max_length=20, choices=UTILITY_CHOICES)
    user_id = models.IntegerField()

    def __str__(self):
        return f'Услуга: {self.utility_type} {self.account_number}'
