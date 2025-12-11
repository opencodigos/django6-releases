from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('toggle/<int:pk>/', views.toggle_tarefa, name='toggle_tarefa'),
    path('api/tarefas/', views.api_tarefas, name='api_tarefas'),
]
