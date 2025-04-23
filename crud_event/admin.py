from django.contrib import admin
from .models import evenement,participation


class evenementAdmin(admin.ModelAdmin):
    list_display = ('nom_event', 'date', 'lieu', 'categorie', 'description', 'organisateur_name')
    search_fields = ('nom_event', 'lieu', 'categorie')
    list_filter = ('date', 'categorie')


class participantAdmin(admin.ModelAdmin):
    list_display = ('participan', 'event', 'date_inscription', 'phone_num', 'name_event', 'participant')
    search_fields = ('participant', 'name_event')
    list_filter = ('date_inscription', 'event__categorie')

admin.site.register(evenement,evenementAdmin)
admin.site.register(participation,participantAdmin)


from django.contrib import admin

admin.site.site_header = "Administration Événements"
admin.site.site_title = "Back Office"
admin.site.index_title = "Tableau de bord de gestion"
