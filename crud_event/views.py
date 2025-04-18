from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse
from .models import evenement
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import CustomUserCreationForm,evenement,EvenementForm  # Importez le formulaire personnalisé
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    evenements = evenement.objects.all()  # Fetch all events from the database
    return render(request, 'home.html', {'evenements': evenements})

def creer_evenement(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('home')  # à adapter selon ton URL de redirection
        
        else:
            messages.error(request, "Donnes invalide")
    else:
         form = EvenementForm()
   
    return render(request, 'creerEvent.html', {'form': form})


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

    return render(request, 'home.html', {'form': form})
        
def liste_evenements(request):
    evenements = evenement.objects.all()
    return render(request, 'home.html', {'evenements': evenements})


    