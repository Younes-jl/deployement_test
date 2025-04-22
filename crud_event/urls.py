from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('creerEvent/', views.creer_evenement, name='creerEvent'),
    path('evenements/', views.liste_evenements, name='home'),
   # path('todos/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('register_evenements/<int:event_id>/', views.register_event, name='register_event'),

]

