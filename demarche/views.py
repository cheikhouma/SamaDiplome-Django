from django.shortcuts import render, redirect
from django.contrib import messages

from securite.forms import ProfileForm
from .form import RecuperationDiplomeForm

def recuperation_diplome(request):
    if request.method == 'POST':
        form = RecuperationDiplomeForm(request.POST, request.FILES, user=request.user)
        
        if form.is_valid():
            form.save()
            # messages.success(request, 'Votre demande a été soumise avec succès.')
            return redirect('confirmation')
    else:
        form = RecuperationDiplomeForm(user=request.user)
    
    return render(request, 'navigation/demarche.html', {'form': form})

def confirmation(request):
    return render(request, 'navigation/validation.html')