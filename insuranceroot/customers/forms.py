from django import  forms


class CustomerForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField()