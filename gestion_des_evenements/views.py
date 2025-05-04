from pyexpat.errors import messages
from django.shortcuts import render,HttpResponse
# from .models import evenement
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from .models import CustomUserCreationForm  # Importez le formulaire personnalisé
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

# def main_page(request):
#     return HttpResponse("Hello world")

# def home(request):
#     return render(request,"home.html")



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser:
                    return redirect(reverse('mon_dashboard'))
                else:
                    login(request, user)
                    return redirect('home')
        
        # Afficher l'erreur ici directement, peu importe la raison
        messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



# @staff_member_required
# def dashboard(request):
#         return render(request, 'dashboard.html')





def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if not form.is_valid():
            # Si le formulaire est invalide, renvoyer les erreurs sous chaque champ
            return render(request, 'signup.html', {'form': form})

        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(request, username=username, password=password)

        if user is None:
            # Si l'utilisateur ne peut pas être authentifié, renvoyer sans message d'erreur
            return render(request, 'signup.html', {'form': form})

        login(request, user)
        
        return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})





def logout_view(request):
    if request.method == 'POST':
        django_logout(request)
        return redirect('home')  # Assure-toi que l'URL "home" existe bien
    return render(request, 'home.html')











