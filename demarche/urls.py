from django.urls import path
from . import views

urlpatterns = [
    path('', views.recuperation_diplome, name="demarche"),
    path('confirmation/', views.confirmation, name="confirmation"),
]