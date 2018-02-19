
from django.shortcuts import redirect, render


def home(request):
    if (request.user.is_authenticated):
        return redirect('/tareas/')
    else:
        return redirect('/accounts/login/')
