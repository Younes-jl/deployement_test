from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
import os
# Create your models here.

def file_path(instance, filename):
    timenow = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Safe filename creation
    filename = f"{timenow}_{filename}"
    return os.path.join('uploads', filename)

class personne(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    num_tel = models.IntegerField() 

class organisateur(personne):
    email = models.EmailField(max_length=200, unique=True)
    description = models.TextField()


class evenement(models.Model):
    id = models.AutoField(primary_key=True)
    nom_event = models.CharField(max_length=200)
    image = models.ImageField(upload_to=file_path, blank=True, null=True)
    date = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")

def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user