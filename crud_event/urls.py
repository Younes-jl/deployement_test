from django.urls import path
from . import views

urlpatterns = [
    path('creer/', views.creer_organisateur, name='home'),
   
   # path('todos/<int:todo_id>/', views.todo_detail, name='todo_detail'),
]

