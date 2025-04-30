from django import forms
from .models import RecuperationDiplome

class RecuperationDiplomeForm(forms.ModelForm):
    date_naissance = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={
                'class': 'form-control',
                'placeholder': 'Exemple : 15-02-2003'
            }
        )
    )

    class Meta:
        model = RecuperationDiplome
        fields = [
            'prenom', 'nom', 'telephone', 'email', 'date_naissance',
            'adresse', 'numero_table', 'annee_bac',
            'lettre_demande', 'attestation_diplome'
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Style Bootstrap pour tous les champs
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'form-control'

        # Ajouts spécifiques
        self.fields['numero_table'].widget.attrs.update({'placeholder': 'Exemple : 123456'})
        self.fields['annee_bac'].widget.attrs.update({'placeholder': 'Exemple : 2020'})
        self.fields['telephone'].widget.attrs.update({'placeholder': 'Exemple : +221774189439'})

        if user and user.is_authenticated:
            self.fields['prenom'].widget.attrs.update({'value': user.first_name})
            self.fields['nom'].widget.attrs.update({
                'placeholder': user.last_name,
                'value': user.last_name
            })
            self.fields['email'].widget.attrs.update({
                'placeholder': user.email,
                'value': user.email
            })
