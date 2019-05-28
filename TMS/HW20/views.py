from django.shortcuts import (
    render,
    redirect,
)
from django.http import HttpResponse
from HW20.forms import CreateNewCarForm
from HW20.models import Car

# Create your views here.


def home(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'home.html', context)


def create_new_car(request):
    if request.method == 'GET':
        context = {'form': CreateNewCarForm()}
        return render(request, 'add.html', context)
    elif request.method == 'POST':
        form = CreateNewCarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            brand = data.get('brand')
            model = data.get('model')
            color = data.get('color')
            weight = data.get('weight')
            full_owner_name = data.get('full_owner_name')
            year_of_manufacture = data.get('year_of_manufacture')
            Car.objects.create(
                brand=brand,
                model=model,
                color=color,
                weight=weight,
                full_owner_name=full_owner_name,
                year_of_manufacture=year_of_manufacture,
            )
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')


def remove_car(request, car_id):
    car = Car.objects.get(id=car_id)
    print(f'{car.brand} {car.model} (owner - {car.full_owner_name}) has been removed')
    car.delete()
    return redirect('home')


def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'GET':
        context = {
            'car_id': car_id,
            'form': CreateNewCarForm(
                initial={
                    'brand': car.brand,
                    'model': car.model,
                    'color': car.color,
                    'weight': car.weight,
                    'full_owner_name': car.full_owner_name,
                    'year_of_manufacture': car.year_of_manufacture,

                }
            )
        }
        return render(request, 'edit.html', context)
    elif request.method == 'POST':
        form = CreateNewCarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            brand = data.get('brand')
            model = data.get('model')
            color = data.get('color')
            weight = data.get('weight')
            full_owner_name = data.get('full_owner_name')
            year_of_manufacture = data.get('year_of_manufacture')
            Car.objects.filter(id=car_id).update(
                brand=brand,
                model=model,
                color=color,
                weight=weight,
                full_owner_name=full_owner_name,
                year_of_manufacture=year_of_manufacture,
            )
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')
