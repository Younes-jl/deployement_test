from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
import os
import datetime
from django.contrib.auth.models import User
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
    image = models.ImageField(upload_to=file_path, blank=True, null=True)
    date = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200)
    description = models.TextField(max_length=2000 , blank=True, null=True)


class participation(models.Model):
      participan=models.ForeignKey(User,on_delete=models.CASCADE)
      event=models.ForeignKey(evenement, on_delete=models.CASCADE)
      date_inscription = models.DateTimeField(auto_now_add=True)
      phone_num=models.CharField(max_length=200, blank=True, null=True)
      name_event=models.CharField(max_length=200, blank=True, null=True)
      participant=models.CharField(max_length=200, blank=True, null=True)
      
      

      def __str__(self):
        return f"{self.participan.username} participe à l'evenement de  {self.event.nom_event}"

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = participation
        fields = ['phone_num']
        widgets = {
            'phone_num': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre numéro de téléphone'})
        }

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
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }