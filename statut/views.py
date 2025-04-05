from django.shortcuts import render
from django import views

class StatutView(views.View):
    def get(self, request, username=None):
        return render(request, "statut/statut.html", {"username": username})