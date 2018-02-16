from django.db import models
from worker.unidad.models import Unidad


class Type_Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner_unit = models.ForeignKey(Unidad, on_delete=models.CASCADE)


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    type_task = models.ForeignKey(Type_Task, on_delete=models.CASCADE)


class Time_Task(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    total = models.TimeField()
    notes = models.CharField(max_length=500)
    total_task = models.TimeField(null=True)

