from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('creer/', views.creer_organisateur, name='createEvent'),
=======
    path('creer/', views.creer_organisateur, name='home'),
>>>>>>> 4c8a262a252c26d1b82bc524b4b37dc69a2816d0
   
   # path('todos/<int:todo_id>/', views.todo_detail, name='todo_detail'),
]

