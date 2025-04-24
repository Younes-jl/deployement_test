
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth.models import User

from crud_event.models import evenement,participation

@staff_member_required
def mon_dashboard(request):

    nb_users = User.objects.count()
    nb_events = evenement.objects.count()
    return render(request, 'dashboard.html',{'nb_users':nb_users,'nb_events':nb_events})

@staff_member_required
def admin_events(request):
    evenements = evenement.objects.all()
    return render(request, 'admin_events.html', {'evenements': evenements})

@staff_member_required
def admin_users(request):
    utilisateurs = User.objects.all()
    return render(request, 'admin_users.html', {'utilisateurs': utilisateurs})

@staff_member_required
def admin_participations(request):
    participations = participation.objects.all  # Use select_related for optimization
    return render(request, 'admin_participations.html', {'participations': participations})


