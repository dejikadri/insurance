from django import forms


def check_name(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name cannot be empty')


class AgentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    phone_number = forms.CharField()
