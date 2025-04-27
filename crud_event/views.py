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
    

@login_required
def participation_history(request):
    participations = participation.objects.filter(participan=request.user).order_by('-date_inscription')
    return render(request, 'historique.html', {'participations': participations})





@login_required
def annuler_participation(request, participation_id):
    participation_instance = get_object_or_404(participation, id=participation_id, participan=request.user)
    participation_instance.delete()
    messages.success(request, "Votre participation a été annulée avec succès.")
    return redirect('history')  # Redirection vers la liste après 