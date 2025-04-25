# urls.py

from django.urls import path
from . import views 
from .views import (
   EventListView, EventCreateView, EventUpdateView, EventDeleteView,
    ParticipationListView, ParticipationDeleteView,
    UserListView, UserUpdateView, SupprimerUtilisateurView,
    ParticipationCreateView, ParticipationUpdateView,AjouterUtilisateurView 
    ,ParticipationCreateView
)


urlpatterns = [
   
  path('dashboard/', views.mon_dashboard, name='mon_dashboard'),
   path('admin_events/', views.admin_events, name='admin_events'),
   path('admin_users/', views.admin_users, name='admin_users'),
   path('admin_participations/', views.admin_participations, name='admin_participations'),
# Event URLs
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/create/', EventCreateView.as_view(), name='event_create'),
    path('events/update/<int:pk>/', EventUpdateView.as_view(), name='event_update'),
    path('events/delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
# Participation URLs
    path('participations/', ParticipationListView.as_view(), name='participation_list'),
     path('participations/create/', ParticipationCreateView.as_view(), name='participation_create'),
    path('participations/update/<int:pk>/', ParticipationUpdateView.as_view(), name='participation_update'),
    path('participations/delete/<int:pk>/', ParticipationDeleteView.as_view(), name='participation_delete'),

# User URLs
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/supprimer/<int:pk>/', SupprimerUtilisateurView.as_view(), name='supprimer_utilisateur'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='modifier_utilisateur'),
    path('users/ajouter/', AjouterUtilisateurView.as_view(), name='ajouter_utilisateur'),

# Events validation

    path('evenements-en-attente/', views.evenements_en_attente, name='evenements_en_attente'),
    path('valider-evenement/<int:id>/', views.valider_evenement, name='valider_evenement'),  # URL pour la validation
]

