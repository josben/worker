from django.db import models
from unidad.models import Unidad


class Type_Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    owner_unit = models.ForeignKey(Unidad, on_delete=models.CASCADE)


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, null=True)
    type_task = models.ForeignKey(Type_Task,
                                  models.SET_NULL,
                                  blank=True,
                                  null=True)


class Tracking(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    total = models.TimeField()
    notes = models.CharField(max_length=500, null=True)
    total_task = models.TimeField(null=True)
