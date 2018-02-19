from django.db import models
from unidad.models import Unidad
from empleado.models import Empleado

import datetime


class Type_Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=700, null=True, blank=True)
    owner_unit = models.ForeignKey(Unidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    owner = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    description = models.CharField(max_length=700, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    is_open = models.BooleanField(default=True)
    type_task = models.ForeignKey(Type_Task,
                                  models.SET_NULL,
                                  blank=True,
                                  null=True)

    def __str__(self):
        return self.name

    def tracking(self):
        return Tracking.objects.filter(task=self)

    def close_task(self):
        self.is_open = False
        self.save()

    def open_task(self):
        self.is_open = True
        self.save()


class Tracking(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time_start = models.TimeField(auto_now_add=True)
    time_end = models.TimeField(null=True, blank=True)
    date_end = models.DateField(auto_now=True)
    total = models.TimeField(null=True, blank=True)
    notes = models.CharField(max_length=700, null=True, blank=True)
    total_task = models.TimeField(null=True, blank=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.task.name + ' (' + str(self.id) + ')'

    def close_tracking(self):
        self.time_end = datetime.datetime.time(datetime.datetime.now())
        self.is_open = False
        self.save()
