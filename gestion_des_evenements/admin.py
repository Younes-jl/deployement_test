from django.contrib import admin
# Register your models here.

# admin.site.register(evenement)
# admin.site.register(utilisateur)

class evenementAdmin(admin.ModelAdmin):
    list_display = ('nom_event', 'date', 'lieu', 'categorie', 'description', 'organisateur')
    search_fields = ('nom_event', 'lieu', 'categorie')
    list_filter = ('date', 'lieu', 'categorie')
    ordering = ('-date',)
    date_hierarchy = 'date'
    list_per_page = 10
    list_editable = ('lieu', 'categorie')

class participationAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_id', 'date_inscription', 'phone_num')
    search_fields = ('name__username', 'event_id__nom_event')
    list_filter = ('date_inscription',)
    ordering = ('-date_inscription',)
    date_hierarchy = 'date_inscription'
    list_per_page = 10
    list_editable = ('phone_num',)