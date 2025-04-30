from django import forms 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignupStep1Form(forms.Form):
    prenom = forms.CharField(min_length=2, max_length=100)
    nom = forms.CharField(max_length=100)
    username = forms.CharField(max_length=150)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur est déjà pris.")
        return username
    

class SignupStep2Form(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    telephone = forms.CharField(
        label="Téléphone",
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Téléphone', 'class': 'form-control'})
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe', 'class': 'form-control'}),
        min_length=6
    )
    confirm_password = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput(attrs={'placeholder': 'Répéter le mot de passe', 'class': 'form-control'})
    )

    accept_terms = forms.BooleanField(
        required=True,
        error_messages={'required': "Veuillez accepter les conditions d'utilisation."},
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Les mots de passe ne correspondent pas.")
        
        return cleaned_data

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['telephone']
        widgets = {
            'telephone': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Téléphone'
            }),
        }
