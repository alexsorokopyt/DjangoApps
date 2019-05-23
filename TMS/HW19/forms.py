from django import forms


CITIES = ['Belarus', 'Russia', 'Ukraine', 'Latvia', 'Lithuania', 'Poland']


class OrderForm(forms.Form):
    name = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    departure_city = forms.ChoiceField(choices=CITIES)
    arrival_city = forms.ChoiceField(choices=CITIES)
    number_of_passengers = forms.IntegerField(min_value=1, max_value=300)
    # departure_date = forms.DateField(help_text='Enter the date of your departure', input_formats='%m/%d/%Y')
