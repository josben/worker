from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Task, Tracking
from empleado.models import Empleado
import datetime


def tasks(request):
    empleado = Empleado.objects.get(user=request.user)
    user_tasks = Task.objects.filter(owner=empleado).filter(create_date=datetime.date.today())
    template = loader.get_template('tareas/tasks.html')
    context = {
        'user_tasks': user_tasks,
    }
    return HttpResponse(template.render(context, request))


def new(request):
    try:
        name_task = request.POST['id_newtask']
    except (Exception):
         return render(request, 'tareas/tasks.html',
                       {'error_message': "No se pudo crear la tarea"})

    open_tasks = Task.objects.filter(is_open=True)
    if (open_tasks):
        open_tasks[0].is_open = False
        open_tasks[0].save()
        tracking = Tracking.objects.filter(task=open_tasks[0]).filter(is_open=True)
        tracking[0].close_tracking()

    empleado = Empleado.objects.get(user=request.user)
    task = Task(owner=empleado, name=name_task)
    task.save()
    tracking = Tracking(task=task)
    tracking.save()

    return redirect('/tareas/')


def stop_tracking(request, tracking_id):
    tracking = Tracking.objects.get(id=tracking_id)
    tracking.time_end = datetime.datetime.time(datetime.datetime.now())
    tracking.is_open = False
    tracking.save()
    tracking.task.close_task()

    return redirect('/tareas/')


def start_tracking(request, tracking_id):
    tracking_old = Tracking.objects.get(id=tracking_id)
    tracking_new = Tracking(task=tracking_old.task)
    tracking_new.save()
    tracking_new.task.open_task()

    return redirect('/tareas/')

