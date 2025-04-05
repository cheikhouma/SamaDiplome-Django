from django import forms 
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ChangePasswordForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    new_password_confirmation = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        new_password = cleaned_data.get("new_password")
        new_password_confirmation = cleaned_data.get("new_password_confirmation")

        print("====\n{}\n=====\n".format(password))
        # Let's authentificate the user
        if authenticate(username=username, password=password) == None:
            raise ValidationError("Le mot de pass est incorrect.")

        # Verify if the new password match with the confirmation password. 
        # Note that the password equality issupposed to be done in the client. We do it again for security
        # reason though.
        if new_password != new_password_confirmation:
            raise ValidationError("Le nouveau mot de passe et sa confirmation ne colle pas du tout!")

        return cleaned_data

        