from django import forms
from .models import Contatto
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'cognome': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Compila questo campo', 'class': 'form-control'}),
            'contenuto': forms.Textarea(attrs={'placeholder': 'Area testuale scrivi pure', 'class': 'form-control'})
        }

    def clean_contenuto(self):
        dati = str.lower(self.cleaned_data["contenuto"])
        if "parola" in dati:
            raise ValidationError("Il contenuto viola le norme del sito")
        if len(dati) < 20:
            raise ValidationError("Il contenuto inserito è troppo breve")
        return dati


class FormRegistrazione(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]
