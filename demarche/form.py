# from django import forms
# from .models import DemandeRecuperationDiplome

# class DemandeForm(forms.ModelForm):
#     class Meta:
#         model = DemandeRecuperationDiplome
#         fields = '__all__'

# from django import forms
# from .models import DiplomeRequest

# class DiplomeRequestForm(forms.ModelForm):
#     date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

#     class Meta:
#         model = DiplomeRequest
#         fields = '__all__'
#         widgets = {
#             'prenom': forms.TextInput(attrs={'placeholder': 'Prénom'}),
#             'nom': forms.TextInput(attrs={'placeholder': 'Nom'}),
#             'telephone': forms.TextInput(attrs={'placeholder': 'Téléphone'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
#             'adresse': forms.TextInput(attrs={'placeholder': 'Adresse'}),
#             'numero_table': forms.TextInput(attrs={'placeholder': 'Numéro de table'}),
#             'annee_bac': forms.NumberInput(attrs={'placeholder': "Année d'obtention du bac"}),
#         }
# class DiplomeRequestForm(forms.ModelForm):
#     date_naissance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'input'}))

#     class Meta:
#         model = DiplomeRequest
#         fields = '__all__'
#         widgets = {
#             'prenom': forms.TextInput(attrs={'class': 'input'}),
#             'nom': forms.TextInput(attrs={'class': 'input'}),
#             'telephone': forms.TextInput(attrs={'class': 'input'}),
#             'email': forms.EmailInput(attrs={'class': 'input'}),
#             'adresse': forms.TextInput(attrs={'class': 'input'}),
#             'numero_table': forms.TextInput(attrs={'class': 'input'}),
#             'annee_bac': forms.NumberInput(attrs={'class': 'input'}),
#             'lettre_demande': forms.ClearableFileInput(attrs={'class': 'input'}),
#             'attestation_diplome': forms.ClearableFileInput(attrs={'class': 'input'}),
#         }

# from django import forms
# from .models import DiplomeForm

# class DiplomeFormForm(forms.ModelForm):
#     class Meta:
#         model = DiplomeForm
#         fields = '__all__'
#         widgets = {
#             'prenom': forms.TextInput(attrs={'placeholder': 'Oumar Faly', 'class': 'form-control'}),
#             'nom': forms.TextInput(attrs={'placeholder': 'Ndiaye', 'class': 'form-control'}),
#             'telephone': forms.TextInput(attrs={'placeholder': '+221 77 137 89 10', 'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'ndiayeof@ept.sn', 'class': 'form-control'}),
#             'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
#             'adresse': forms.TextInput(attrs={'placeholder': 'Adresse', 'class': 'form-control'}),
#             'numero_table': forms.TextInput(attrs={'placeholder': '36 420', 'class': 'form-control'}),
#             'annee_bac': forms.NumberInput(attrs={'placeholder': '1999', 'class': 'form-control'}),
#         }



from django import forms
from .models import RecuperationDiplome

class RecuperationDiplomeForm(forms.ModelForm):
    class Meta:
        model = RecuperationDiplome
        fields = ['prenom', 'nom', 'telephone', 'email', 'date_naissance', 
                  'adresse', 'numero_table', 'annee_bac', 
                  'lettre_demande', 'attestation_diplome']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajout des placeholders
        self.fields['prenom'].widget.attrs.update({'placeholder': 'Oumar Faly', 'class': 'form-control'})
        self.fields['nom'].widget.attrs.update({'placeholder': 'Ndiaye', 'class': 'form-control'})
        self.fields['telephone'].widget.attrs.update({'placeholder': '+221 77 137 89 10', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'ndiayeof@ept.sn', 'class': 'form-control'})
        self.fields['adresse'].widget.attrs.update({'placeholder': 'Adresse', 'class': 'form-control'})
        self.fields['numero_table'].widget.attrs.update({'placeholder': '36 420', 'class': 'form-control'})
        self.fields['annee_bac'].widget.attrs.update({'placeholder': '1999', 'class': 'form-control'})
        self.fields['date_naissance'].widget.attrs.update({'class': 'form-control'})
        self.fields['lettre_demande'].widget.attrs.update({'class': 'form-control'})
        self.fields['attestation_diplome'].widget.attrs.update({'class': 'form-control'})