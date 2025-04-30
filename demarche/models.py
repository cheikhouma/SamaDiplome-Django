# from django.db import models

# class DemandeRecuperationDiplome(models.Model):
#     prenom = models.CharField(max_length=100)
#     nom = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=20)
#     email = models.EmailField()
#     date_naissance = models.DateField()
#     adresse = models.CharField(max_length=255)
#     numero_table = models.CharField(max_length=50)
#     annee_bac = models.IntegerField()
#     lettre_demande = models.FileField(upload_to='documents/')
#     attestation_diplome = models.FileField(upload_to='documents/')
#     date_soumission = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.prenom} {self.nom} - {self.annee_bac}"

# from django.db import models

# class DiplomeRequest(models.Model):
#     prenom = models.CharField(max_length=100)
#     nom = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=20)
#     email = models.EmailField()
#     date_naissance = models.DateField()
#     adresse = models.TextField()
#     numero_table = models.CharField(max_length=50)
#     annee_bac = models.IntegerField()
#     lettre_demande = models.FileField(upload_to='documents/demandes/')
#     attestation_diplome = models.FileField(upload_to='documents/attestations/')

#     def __str__(self):
#         return f"{self.prenom} {self.nom} - {self.numero_table}"

# from django.db import models

# class DiplomeForm(models.Model):
#     prenom = models.CharField(max_length=100)
#     nom = models.CharField(max_length=100)
#     telephone = models.CharField(max_length=20)
#     email = models.EmailField()
#     date_naissance = models.DateField()
#     adresse = models.CharField(max_length=255)
#     numero_table = models.CharField(max_length=50)
#     annee_bac = models.IntegerField()
#     lettre_demande = models.FileField(upload_to='lettres/')
#     attestation_diplome = models.FileField(upload_to='attestations/')

#     def __str__(self):
#         return f"{self.prenom} {self.nom}"

from django.db import models

class RecuperationDiplome(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=255)
    numero_table = models.IntegerField()
    annee_bac = models.IntegerField()
    lettre_demande = models.FileField()
    attestation_diplome = models.FileField()
    
    # lettre_demande = models.FileField(upload_to='lettres_demande/')
    # attestation_diplome = models.FileField(upload_to='attestations_diplome/')
    date_soumission = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.annee_bac}"