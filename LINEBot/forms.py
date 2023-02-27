from django import forms

class driverForm(forms.Form):
    user_id = forms.CharField(max_length=20, required=True)
    driver_id= forms.CharField(max_length=20, required=True)
    phone_number = forms.CharField(max_length=20, required=True)