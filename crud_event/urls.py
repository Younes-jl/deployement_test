from django.urls import path
from . import views

urlpatterns = [
    #path('home/', views.home, name='home'),
    #path('ce/', views.liste_evenements, name='home'),

    path('', views.home, name='home'),
    path('creerEvent/', views.creer_evenement, name='creerEvent'),
    path('register_evenements/<int:event_id>/', views.register_event, name='register_event'),

]

