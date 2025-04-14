from django.urls import path
from . import views

urlpatterns = [
    path('creer/', views.home, name='createEvent'),
   
   # path('todos/<int:todo_id>/', views.todo_detail, name='todo_detail'),
]

