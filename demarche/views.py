# from django.shortcuts import render, redirect
# from .models import DemandeRecuperationDiplome
# from .form import DemandeForm

# # def formulaire_recuperation(request):
# #     if request.method == 'POST':
# #         DemandeRecuperationDiplome.objects.create(
# #             prenom=request.POST.get('prenom'),
# #             nom=request.POST.get('nom'),
# #             telephone=request.POST.get('telephone'),
# #             email=request.POST.get('email'),
# #             date_naissance=request.POST.get('dateNaissance'),
# #             adresse=request.POST.get('adresse'),
# #             numero_table=request.POST.get('numeroTable'),
# #             annee_bac=request.POST.get('anneeBac'),
# #             lettre_demande=request.FILES.get('lettreDemande'),
# #             attestation_diplome=request.FILES.get('attestationDiplome'),
# #         )
# #         return redirect('formulaire_success')
# #     return render(request, 'formulaire.html')

# def formulaire_recuperation(request):
#     print(request.POST)
#     if request.method == 'POST':
#         form = DemandeForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             # return redirect('formulaire_success')  # ou afficher un message
#     else:
#         form = DemandeForm()
#     return render(request, 'navigation/demarche.html', context={'form': form})


# def formulaire_success(request):
#     return render(request, 'success.html')


# from django.shortcuts import render, redirect
# from .form import DiplomeRequestForm

# def demande_diplome(request):
#     if request.method == 'POST':
#         form = DiplomeRequestForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return redirect('confirmation')  # Crée une page de confirmation simple
#     else:
#         form = DiplomeRequestForm()
#     return render(request, 'navigation/demarche.html', {'form': form})

# from django.shortcuts import render, redirect
# from .form import DiplomeFormForm

# def formulaire_view(request):
#     if request.method == 'POST':
#         form = DiplomeFormForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = DiplomeFormForm()
#     return render(request, 'navigation/demarche.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from .form import RecuperationDiplomeForm

def recuperation_diplome(request):
    if request.method == 'POST':
        form = RecuperationDiplomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Votre demande a été soumise avec succès.')
            return redirect('confirmation')
    else:
        form = RecuperationDiplomeForm()
    
    return render(request, 'navigation/demarche.html', {'form': form})

def confirmation(request):
    return render(request, 'navigation/validation.html')