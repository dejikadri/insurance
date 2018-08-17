from django.db import models
from agents.models import Agent


class Customer(models.Model):
    agent = models.ForeignKey(Agent)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
