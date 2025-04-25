from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse
from .models import evenement
from crud_event.models import evenement, participation
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import CustomUserCreationForm,evenement,EvenementForm  # Importez le formulaire personnalisé
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import get_object_or_404
from .models import participation
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.

from django.contrib import messages


@login_required
def creer_evenement(request):
    if request.method == 'POST':
        form = EvenementForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)  
            event.organisateur = request.user
            event.fullname = request.user.username
            event.is_validated = False  # L'événement n'est pas encore validé par l'admin
            event.save()  # Sauvegarder l'événement dans la base de données
            messages.success(request, "Votre événement a été créé avec succès, en attente de validation par l'administrateur.")
            return redirect('creerEvent')  # Rediriger vers la page d'accueil après la création

        else:
            messages.error(request, "Données invalides")  # Afficher un message d'erreur si le formulaire est invalide
    else:
        form = EvenementForm()

    return render(request, 'creerEvent.html', {'form': form})









# def signin(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
        
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                     login(request, user)
#                     return redirect('creerEvent')
        
#         # Afficher l'erreur ici directement, peu importe la raison
#         messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        
#     else:
#              form = AuthenticationForm()

#     return render(request, 'home.html', {'form': form})

def home(request):
    evenements = evenement.objects.filter(is_validated=True)
    return render(request, 'home.html', {'evenements': evenements})


#def liste_evenements(request):
   # evenements = evenement.objects.all()
   # return render(request, 'home.html', {'evenements': evenements})


@login_required
def register_event(request, event_id):
    event = get_object_or_404(evenement, id=event_id)
    if request.method == 'POST':
        name = request.user  # Assuming the user is logged in
        phone_num = request.POST.get('phone_num')
        nom_event = event.nom_event
        nam = request.POST.get('name')
          # Store the username of the logged-in user
        participation_instance = participation.objects.create(participan=name,event=event, name_event = nom_event, phone_num=phone_num,participant=nam )
        participation_instance.save()
        messages.success(request, "Inscription réussie à l'événement.")
        return redirect('home')
    
        # Handle registration logic here (e.g., save to database, send email, etc.)
    return render(request, 'register.html', {'event': event})
    