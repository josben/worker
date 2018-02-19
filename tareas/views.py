from django.shortcuts import render
from .models import Task


def new(request):
    try:
        name_task = request.POST['id_newtask']
    except (Exception):
         return render(request, 'home.html',
                       {'error_message': "No se pudo crear la tarea"})
    task = Task(name=name_task)
    task.save()

    return request(request, 'home.html')
