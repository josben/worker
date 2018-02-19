from django.urls import path
#from django.views.generic.base import TemplateView
from tareas import views

app_name = 'tareas'
urlpatterns = [
#    path('', TemplateView.as_view(template_name='tasks.html'), name='tasks'),
    path('', views.tasks, name='tasks'),
    path('new/', views.new, name='new_task'),
    path('<int:tracking_id>/stop/', views.stop_tracking, name='tracking_stop'),
    path('<int:tracking_id>/start/', views.start_tracking, name='tracking_start'),
]
