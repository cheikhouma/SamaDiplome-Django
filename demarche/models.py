from datetime import date
from django.db import models

class RecuperationDiplome(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    date_naissance = models.DateField(default=date(2003, 2, 15))
    adresse = models.CharField(max_length=255)
    numero_table = models.IntegerField()
    annee_bac = models.IntegerField()
    lettre_demande = models.FileField(upload_to='lettres_demande/')
    attestation_diplome = models.FileField(upload_to='attestations_diplome/')
    date_soumission = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.annee_bac}"