# Создать модель Car. Атрибуты:
# - марка,
# - модель,
# - цвет,
# - вес,
# - полное имя владельца,
# - год выпуска.

from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    weight = models.PositiveIntegerField(validators=[MinValueValidator(500)])
    full_owner_name = models.CharField(max_length=100)
    year_of_manufacture = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2019)])
