from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse
from .models import evenement
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import CustomUserCreationForm  # Importez le formulaire personnalisé
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    return render(request,"home.html")

def creer_organisateur(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organisateur')  # à adapter selon ton URL de redirection
        
        else:
            messages.error(request, "Donnes invalide")
    else:
         form = CustomUserCreationForm()        
   
    
    return render(request, 'organisateur.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                    login(request, user)
                    return redirect('creerEvent')
        
        # Afficher l'erreur ici directement, peu importe la raison
        messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        
    else:
             form = AuthenticationForm()

    return render(request, 'creerEvent.html', {'form': form})
        



    