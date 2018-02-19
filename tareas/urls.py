from django.urls import path
#from django.views.generic.base import TemplateView
from tareas import views

app_name = 'tareas'
urlpatterns = [
#    path('', TemplateView.as_view(template_name='tasks.html'), name='tasks'),
    path('new/', views.new, name='new_tasks'),
]
