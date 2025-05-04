from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
import os
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

# Create your models here.

def file_path(instance, filename):
    timenow = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Safe filename creation
    filename = f"{timenow}_{filename}"
    return os.path.join('uploads', filename)

# class personne(models.Model):
#     id = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=200)
#     prenom = models.CharField(max_length=200)
#     num_tel = models.IntegerField() 

# class organisateur(personne):
#     email = models.EmailField(max_length=200, unique=True)
#     description = models.TextField()


class evenement(models.Model):
    id = models.AutoField(primary_key=True)
    nom_event = models.CharField(max_length=200)
    image = models.ImageField(upload_to=file_path, blank=True, null=True,default='media/ibm.jpg')
    date = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200)
    description = models.TextField(max_length=2000 , blank=True, null=True)
    organisateur = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    organisateur_name = models.CharField(max_length=200, blank=True, null=True)
    is_validated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nom_event
    def save(self, *args, **kwargs):
        if self.organisateur and not self.organisateur_name:
            self.organisateur_name = self.organisateur.username
        super(evenement, self).save(*args, **kwargs)


class participation(models.Model):
      participan=models.ForeignKey(User,on_delete=models.CASCADE)
      event=models.ForeignKey(evenement, on_delete=models.CASCADE)
      date_inscription = models.DateTimeField(default=timezone.now)
      phone_num=models.CharField(max_length=200, blank=True, null=True)
      name_event=models.CharField(max_length=200, blank=True, null=True)
      participant=models.CharField(max_length=200, blank=True, null=True)
      email=models.EmailField(max_length=200, blank=True, null=True)
      def __str__(self):
        return f"{self.participan.username} participe à l'evenement de  {self.event.nom_event}"


class ParticipationForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Add email field
    
    class Meta:
        model = participation
        fields = ['event', 'participan', 'date_inscription', 'phone_num', 'name_event']
        widgets = {
            'date_inscription': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'event': forms.Select(attrs={'class': 'form-control'}),
            'participan': forms.Select(attrs={'class': 'form-control'}),
        }





class paiement(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(evenement,null=True, on_delete=models.CASCADE)  
    participation = models.ForeignKey(participation, on_delete=models.CASCADE, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)  
    card_holder_name = models.CharField(max_length=200, blank=True, null=True)  
    expiry_date = models.DateField(blank=True, null=True)  
    cvv = models.CharField(max_length=3, blank=True, null=True) 
    payment_method = models.CharField(max_length=200, blank=True, null=True)
















class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")

def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EvenementForm(forms.ModelForm):
    class Meta:
        model = evenement
        exclude = ['organisateur', 'organisateur_name', 'is_validated']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                  }

 
 