from django import forms


class CreateNewCarForm(forms.Form):
    brand = forms.CharField(max_length=30)
    model = forms.CharField(max_length=30)
    color = forms.CharField(max_length=30)
    weight = forms.IntegerField(min_value=500)
    full_owner_name = forms.CharField(max_length=100)
    year_of_manufacture = forms.IntegerField(min_value=1900, max_value=2019)
