
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from crud_event.models import evenement,participation
from django import forms
# from crud_event.models import ParticipationCustomForm

@staff_member_required
def mon_dashboard(request):
    nb_users = User.objects.count()
    nb_events = evenement.objects.count()
    nb_participations = participation.objects.count()
    return render(request,'dashboard.html',{'nb_users':nb_users,'nb_events':nb_events,'nb_participations':nb_participations})

# @staff_member_required
# def admin_events(request):
#     evenements = evenement.objects.all()
#     return render(request, 'admin_events.html', {'evenements': evenements})

@staff_member_required
def admin_users(request):
    utilisateurs = User.objects.all()
    return render(request, 'admin_users.html', {'utilisateurs': utilisateurs})

# @staff_member_required
# def admin_participations(request):
#     participations = participation.objects.all  # Use select_related for optimization
#     return render(request, 'admin_participations.html', {'participations': participations})


# -------------------------------------------------------------
# CRUD for events 
class EventListView(ListView):
    model = evenement
    template_name = 'admin_events.html'
    context_object_name = 'events'

class EventCreateView(CreateView):
    model = evenement
    fields = ['nom_event', 'image', 'date', 'lieu', 'categorie', 'description']
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        return form

class EventUpdateView(UpdateView):
    model = evenement
    fields = ['nom_event', 'image', 'date', 'lieu', 'categorie', 'description']
    template_name = 'event_form.html'
    success_url = reverse_lazy('event_list')
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['date'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        return form

class EventDeleteView(DeleteView):
    model = evenement
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('event_list')


# CRUD for Users
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'user_form.html'
    success_url = reverse_lazy('admin_users')  # ou 'user_list' selon ce que tu veux

class SupprimerUtilisateurView(DeleteView):
    model = User
    template_name = 'supprimer_utilisateur.html'
    success_url = reverse_lazy('admin_users')  # ou 'user_list' selon ce que tu veux

class AjouterUtilisateurView(CreateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'password']
    template_name = 'ajouter_utilisateur.html'
    success_url = reverse_lazy('admin_users')  # Redirige vers la liste des utilisateurs après la création

    def form_valid(self, form):
        # Hash the password before saving the user
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)




class ParticipationListView(ListView):
    model = participation
    template_name = "list_particpation.html"
    context_object_name = "participations"
    ordering = ['-date_inscription']  


class ParticipationCreateView(CreateView):
    model = participation
    template_name = "add_participation.html"
    fields = ['participan', 'event', 'phone_num']  # Admin choisit Utilisateur + Evénement + Téléphone
    success_url = reverse_lazy('participations')

    def form_valid(self, form):
        # Remplir automatiquement name_event
        form.instance.name_event = form.instance.event.nom_event
        # Remplir automatiquement participant avec le nom de l'utilisateur
        form.instance.participant = form.instance.participan.get_full_name() or form.instance.participan.username
        return super().form_valid(form)



class ParticipationUpdateView(UpdateView):
    model = participation
    template_name = "edit_participation.html"
    fields = ['participan', 'event', 'phone_num']  # Choix de l'utilisateur, l'événement, et téléphone
    success_url = reverse_lazy('participations')



class ParticipationDeleteView(DeleteView):
    model = participation
    template_name = "delete_participation.html"  # On va créer une page de confirmation
    success_url = reverse_lazy('participations')
















def evenements_en_attente(request):
    # Récupérer tous les événements en attente de validation (supposons que tu as un champ 'valide' qui définit si l'événement est validé ou non)
    evenements = evenement.objects.filter(is_validated=False) # Exemple, adapte en fonction de ton modèle
    return render(request, 'validerEvenements.html', {'evenements': evenements})


def valider_evenement(request, id):
    if request.method == 'POST':
        evt = get_object_or_404(evenement, id=id)
        evt.is_validated = True
        evt.save()
    return redirect('evenements_en_attente')
