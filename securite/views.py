from django.shortcuts import render
from django import views
from django.contrib.auth.models import User
from .import forms
from django.http import HttpResponse, JsonResponse

class ChangePassword(views.View):
    def get(self, request, username=None):
        name = "Nothing Found"
        email = "nothing@found.com"
        if username:
            user = User.objects.get(username=username)
            first_name = user.first_name
            last_name = user.last_name
            name = first_name + " " + last_name
            email = user.email
        else:
            username = "nothing"
        return render(request, "securite/securite.html", {"name": name, "email": email, "username": username})

    def post(self, request, username=None):
        # Check if this is not a deletion request disguised
        if request.POST.get("_method") == "DELETE":
            """ This one is triggered when the user really want to delete its account: pray god won't 
            never happen, we need your data bro!"""
            user = User.objects.get(username=username)
            user.delete()  # good bye data
            return HttpResponse("Ton a ete bel et bien suppirme, contre notre volonte. Tu n'est meme pas reconnaissant!")

        # Feed the form
        form = forms.ChangePasswordForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data.get("username")
            new_password = form.cleaned_data.get("new_password")
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            return HttpResponse("Password changed succesfully!")
        else:
            print(form.errors)
            return HttpResponse("Double check the password bro: there may have an error somewhere.") 

