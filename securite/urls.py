from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('connexion/', views.connexion_step1, name='connexion1'),
    path('connexion2/<int:user_id>/', views.connexion_step2, name='login_step2'),
    # ...other paths
    path('inscription/', views.signup_step1, name='signup_step1'),
    path('inscription2/', views.signup_step2, name='signup_step2'),
    path('securite/validation/', views.signup_validation, name='signup_validation'),
    path('securite/complete/', views.signup_complete, name='signup_complete'),

    path('deconnexion/', views.deconnexion, name='deconnexion'),

    # Profil
    path('profil/infos/', views.infos_perso, name='infos-perso'),
    path('profil/modifier-infos/', views.modifier_infos, name='modifier-infos'),
    path('profil/securite/', views.changer_mot_de_passe, name='securite'),

    path('supprimer-compte/', views.supprimer_compte, name='supprimer_compte'),

    path('mdp-oublie/email', views.password_reset_email, name='email-mdp'),
    path('mdp-oublie/code', views.verify_code, name='code-mdp'),
    path('mdp-oublie/change', views.change_password, name='change-mdp'),
    path('mdp-oublie/validation', views.validation_password, name='validation-mdp'),

    path('compte/infos/', views.infos_perso, name='infos-perso'),
    path('compte/modifier-infos/', views.modifier_infos, name='modifier-infos'),
    path('compte/securite/', views.changer_mot_de_passe, name='securite'),

]

