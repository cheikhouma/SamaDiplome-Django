from django.shortcuts import render, redirect
from django import views
from .import forms
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse 

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms import SignupStep1Form, SignupStep2Form
from django.contrib import messages
from .models import Profile 
from django.db.models import Q



from django.http import HttpResponseRedirect
from django.urls import reverse



def connexion_step1(request):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')

        try:
            # By username / email
            user = User.objects.get(Q(username=identifiant) | Q(email=identifiant))
            return redirect('login_step2', user_id=user.id)
        except User.DoesNotExist:
            return render(request, 'navigation/connexion/connexion.html', {
                'error': "Utilisateur introuvable."
            })

    return render(request, 'navigation/connexion/connexion.html')


def connexion_step2(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return render(request, 'navigation/connexion/connexion2.html', {'error': "Utilisateur introuvable."})
    
    if request.method == 'POST':
        password = request.POST.get('password')
        authenticated_user = authenticate(request, username=user.username, password=password)
        if authenticated_user:
            login(request, authenticated_user)
            return redirect('accueil')
        else:
            return render(request, 'navigation/connexion/connexion2.html', {'user_id': user.id, 'error': "Mot de passe incorrect."})

    return render(request, 'navigation/connexion/connexion2.html', {'user_id': user.id})


def signup_step1(request):
    if request.method == 'POST':
        form = SignupStep1Form(request.POST)
        if form.is_valid():
            request.session['signup_data'] = {
                'prenom': form.cleaned_data['prenom'],
                'nom': form.cleaned_data['nom'],
                'username': form.cleaned_data['username']
            }
            return redirect('signup_step2')
    else:
        form = SignupStep1Form()
    
    return render(request, 'navigation/inscription/inscription1.html', {'form': form})

def signup_step2(request):
    signup_data = request.session.get('signup_data')

    if not signup_data:
        messages.error(request, "Veuillez d'abord remplir la première étape.")
        return redirect('signup_step1')

    if request.method == 'POST':
        form = SignupStep2Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            password = form.cleaned_data['password']

            try:
                user = User.objects.create_user(
                    username=signup_data['username'],
                    first_name=signup_data['prenom'],
                    last_name=signup_data['nom'],
                    email=email,
                    password=password
                )

                profile = Profile(user=user, telephone=telephone)
                profile.save()

                # Auto login
                login(request, user)

                del request.session['signup_data']
                return redirect('signup_validation')

            except Exception as e:
                form.add_error(None, f"Erreur lors de l'inscription: {e}")
                return render(request, 'navigation/inscription/inscription2.html', {'form': form})
    else:
        form = SignupStep2Form()

    return render(request, 'navigation/inscription/inscription2.html', {'form': form})



def signup_validation(request):
    return render(request, 'navigation/inscription/validation.html')

def signup_complete(request):
    return render(request, 'navigation/inscription/complete.html')

def deconnexion(request):
    logout(request) 
    # Clear session
    request.session.flush()  
    return redirect('connexion1') 


# Profil ---------------------------------------------------------------


@login_required
def infos_perso(request):
    template = 'navigation/profil/infos-perso.html'
    if request.GET.get('mobile') == '1':
        template = 'navigation/profil/infos-phone.html'
    return render(request, template, {'user': request.user})


from .models import Profile
from .forms import ProfileForm
@login_required
def modifier_infos(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()


            redirect_url = reverse('infos-perso')
            if request.GET.get('mobile') == '1':
                redirect_url += '?mobile=1' 
            return HttpResponseRedirect(redirect_url) 

    else:
        profile_form = ProfileForm(instance=profile)

    template = 'navigation/profil/modifier-infos.html'
    if request.GET.get('mobile') == '1':
        template = 'navigation/profil/modifier-phone.html'

    return render(request, template, {
        'user': user,
        'profile_form': profile_form
    })



# Password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def changer_mot_de_passe(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            redirect_url = reverse('infos-perso')
            if request.GET.get('mobile') == '1':
                redirect_url += '?mobile=1'
            return HttpResponseRedirect(redirect_url)

    else:
        form = PasswordChangeForm(user=request.user)

    template = 'navigation/profil/securite.html'
    if request.GET.get('mobile') == '1':
        template = 'navigation/profil/securite-phone.html'

    return render(request, template, {'form': form})




@login_required
def supprimer_compte(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect('connexion1')


from django.contrib.auth.forms import PasswordResetForm

def password_reset_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        from django.contrib.auth import get_user_model
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
            # Fake code simulation
            request.session['otp_code'] = '12345'
            request.session['reset_email'] = email
            return redirect('code-mdp')
        except User.DoesNotExist:
            messages.error(request, "Aucun compte n'est associé à cet email.")
    
    return render(request, 'navigation/mdp-oublie/email-mdp.html')


def verify_code(request):
    if request.method == 'POST':
        code = ''.join([request.POST.get(f'digit{i}', '') for i in "12345"])
        if code == request.session.get('otp_code'):
            return redirect('change-mdp')
        else:
            messages.error(request, "Code invalide. Réessayez 12345 (simulation test).")
    return render(request, 'navigation/mdp-oublie/code-mdp.html')


from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


def change_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'navigation/mdp-oublie/change-mdp.html')

        email = request.session.get('reset_email')
        if not email:
            messages.error(request, "Session expirée. Recommencez.")
            return redirect('email-mdp')

        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            user.password = make_password(new_password)
            user.save()

            logout(request)
            return redirect('validation-mdp')
        except User.DoesNotExist:
            messages.error(request, "Utilisateur introuvable.")

    return render(request, 'navigation/mdp-oublie/change-mdp.html')



def validation_password(request):
    return render(request, 'navigation/mdp-oublie/validation-mdp.html')

