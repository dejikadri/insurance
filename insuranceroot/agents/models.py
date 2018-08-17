from django.db import models


class Agent(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=700)
    phone_number = models.CharField(max_length=30)
    active_status = models.PositiveSmallIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'



'''



class Payment(models.Model):
    
    vehicle(foreignkey)
    product(foreignkey)
    agent(foreignkey)
    amount
    paymentdate on
    

    amount = models.DecimalField(max_digits=10 ,decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
'''
