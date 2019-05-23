# Создать форму через django forms описывающую заказ авиабилета.
# Форма должна содержать следующие поля - имя, откуда, куда, сколько человек, дата.
# При отправке данных пользователем проверять валидность данных,
# если они валидны и количество человек равно 1 то вывести результат - "стоимость 100$",
# если количество человек больше 1, то стоимость должна считаться по формуле 100*2*количество человек.
# Если данные не валидны, то вывести ошибку.


from django.shortcuts import render
from django.http import HttpResponse
from HW19.forms import OrderForm

FORM = OrderForm()
BASIC_COST_OF_TICKET = 100
CURRENCY = '$'


def ticket_order(request):
    if request.method == 'GET':
        return render(request, 'tickets_main_page.html', {'form': FORM})
    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # name = data.get('name')
            # lastname = data.get('lastname')
            # departure_city = data.get('departure_city')
            # arrival_city = data.get('arrival_city')
            number_of_passengers = data.get('number_of_passengers')
            # departure_date = data.get('departure_date')
            if number_of_passengers == 1:
                cost_of_one_ticket = BASIC_COST_OF_TICKET
                result = f'{CURRENCY}{cost_of_one_ticket}'
            elif number_of_passengers >= 2:
                cost_of_one_ticket = BASIC_COST_OF_TICKET * 2
                cost_of_all_tickets = cost_of_one_ticket * number_of_passengers
                result = f'{CURRENCY}{cost_of_all_tickets}'
            print(result)
            return render(request, 'tickets_main_page.html', {'form': FORM})
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')
