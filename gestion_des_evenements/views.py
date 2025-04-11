from django.shortcuts import render,HttpResponse
from .models import evenement
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import CustomUserCreationForm  # Importez le formulaire personnalisé

# Create your views here.

def main_page(request):
    return HttpResponse("Hello world")

def home(request):
    return render(request,"home.html")

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser:
                    return redirect(reverse('admin:index'))
                else:
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            messages.error(request, "Formulaire invalide. Veuillez réessayer.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})





def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form})

        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(request, username=username, password=password)

        if user is None:
            return HttpResponse("Erreur d'authentification")

        login(request, user)
        return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


def todos(request):
    items = evenement.objects.all()
    return render(request,"Todo.html",{"todos":items})
