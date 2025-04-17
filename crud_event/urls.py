from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('creerEvent/', views.creer_evenement, name='creerEvent'),
   
   # path('todos/<int:todo_id>/', views.todo_detail, name='todo_detail'),
]

