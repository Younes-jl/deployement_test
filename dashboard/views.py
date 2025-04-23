
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib.auth.models import User

from crud_event.models import evenement

@staff_member_required
def mon_dashboard(request):

    nb_users = User.objects.count()
    nb_events = evenement.objects.count()
    return render(request, 'dashboard.html',{'nb_users':nb_users,'nb_events':nb_events})

