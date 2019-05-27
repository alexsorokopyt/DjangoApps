from django.urls import path
from CW20.views import home_page

urlpatterns = [
    path('home/', home_page, name='home'),
]
