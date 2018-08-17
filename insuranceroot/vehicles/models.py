from django.db import models
from agents.models import Agent
from customers.models import Customer


class Vehicles(models.Model):
    agent = models.ForeignKey(Agent)
    customer = models.ForeignKey(Customer)
    policy_number = models.CharField(max_length=120, unique=True)
    engine_no = models.CharField(max_length=120)
    registration_no = models.CharField(max_length=100, unique=True)
    vehicle_make = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    policy_expiry_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.vehicle_make}-{self.vehicle_model} - {self.registration_no}'


class Product(models.Model):
    product_code = models.CharField(max_length=20)
    product_name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.product_code


class Payment(models.Model):
    agent = models.ForeignKey(Agent)
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    vehicle = models.ForeignKey(Vehicles)
    policy_number = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.policy_number} - {self.amount}'
