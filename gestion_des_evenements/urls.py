from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('home/', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
path('logout/', views.logout_view, name='logout')
   # path('todos/<int:todo_id>/', views.todo_detail, name='todo_detail'),
]

