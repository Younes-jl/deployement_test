from django.urls import path
from . import views

urlpatterns = [
    #path('home/', views.home, name='home'),
    #path('ce/', views.liste_evenements, name='home'),

    path('', views.home, name='home'),
    path('creerEvent/', views.creer_evenement, name='creerEvent'),
    path('register_evenements/<int:event_id>/', views.register_event, name='register_event'),
    path('history/', views.participation_history, name='history'),
     path('annuler/<int:participation_id>/', views.annuler_participation, name='cancel_participation'),

]

