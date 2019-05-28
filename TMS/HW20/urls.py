from django.urls import path
from HW20.views import (
    home,
    create_new_car,
    remove_car,
    edit_car,
)


urlpatterns = [
    path('home/', home, name='home'),
    path('add/', create_new_car, name='new_car'),
    path('remove/<int:car_id>', remove_car, name='delete'),
    path('edit/<int:car_id>', edit_car, name='edit'),
]
