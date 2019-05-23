from django import forms
from HW19.cities_with_airports import CITIES


class OrderForm(forms.Form):
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    departure_city = forms.CharField(widget=forms.Select(choices=CITIES))
    arrival_city = forms.CharField(widget=forms.Select(choices=CITIES))
    departure_date = forms.DateField(widget = forms.SelectDateWidget())
    number_of_passengers = forms.IntegerField(min_value=1, max_value=300)
