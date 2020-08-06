from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class Contact_Form(forms.Form):
    name = forms.CharField(max_length = 50)
    email = forms.EmailField(unique = True)
    phone_number = PhoneNumberField()
    address = forms.CharField(max_length = 150)