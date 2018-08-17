from django import forms
from . import models


class VehiclesForm(forms.Form):
    engine_no = forms.CharField()
    registration_no = forms.CharField()
    vehicle_make = forms.CharField()
    vehicle_model = forms.CharField()


class PaymentForm(forms.Form):
    #product = forms.ModelChoiceField(to_field_name='price', empty_label="Select Product", queryset=models.Product.objects.all().order_by('product_code').values_list('product_code'))
    product = forms.ModelChoiceField(empty_label="Select Product", to_field_name="price", queryset=models.Product.objects.only('product_code', 'price').order_by('product_code'))
    #Amount = forms.CharField()

