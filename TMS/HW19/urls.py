from django.urls import path
from HW19.views import ticket_order

urlpatterns = [
    path('new_order/', ticket_order, name='new_order'),
]
