from django.db import models
from unidad.models import Unidad


class Empleado(models.Model):
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    boss = models.ForeignKey('self', on_delete=models.CASCADE)
