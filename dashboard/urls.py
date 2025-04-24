# urls.py

from django.urls import path
from . import views

urlpatterns = [
   
  path('dashboard/', views.mon_dashboard, name='mon_dashboard'),
  path('admin_events/', views.admin_events, name='admin_events'),
  path('admin_users/', views.admin_users, name='admin_users'),
  path('admin_participations/', views.admin_participations, name='admin_participations'),

]

