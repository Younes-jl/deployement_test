# urls.py

from django.urls import path
from . import views

urlpatterns = [
   
  path('dashboard/', views.mon_dashboard, name='mon_dashboard'),

]

