from django.db import models
import datetime
import os
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Helper function to generate a unique file path
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

class utilisateur(personne):
      pass

class evenement(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to=file_path, blank=True, null=True)
    date = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200)

# class billet(models.Model):
#     id = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=200)
#     prenom = models.CharField(max_length=200)

# class compte(models.Model):
#      id = models.AutoField(primary_key=True)
#      email = models.EmailField(max_length=200, unique=True)
#      mot_de_passe = models.CharField(max_length=200)
#      username = models.CharField(max_length=200, unique=True)   

class admin(personne):
      pass


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")
    first_name = forms.CharField(max_length=30, required=True, label="Prénom")
    last_name = forms.CharField(max_length=30, required=True, label="Nom de famille")


    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']
        help_texts = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
            
        }
        def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user