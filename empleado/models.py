from django.db import models
from unidad.models import Unidad
from django.contrib.auth.models import User

class Empleado(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    boss = models.ForeignKey('self', models.SET_NULL,
                             blank=True, null=True)
