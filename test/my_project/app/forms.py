from django import forms
from django.forms import ValidationError
from django.contrib.auth import authenticate

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, label="Adresa de email")
    subiect = forms.CharField(label="Subiectul tau")
    mesaj = forms.CharField(widget=forms.Textarea)
    trimite_copie =forms.BooleanField(required=False, label="Trimite o copie a mesajului")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith("gmail.com"):
            raise forms.ValidationError("Email-ul trebuie sa fie de tip gmail.com")
        return email
    

class CustomLoginForm(forms.Form):
    username = forms.CharField(label="Nume utilizator")
    password = forms.CharField(widget=forms.PasswordInput, label="Parola")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(None, username=username, password=password)
        if user is None:
            raise forms.ValidationError("Numele de utilizator sau parola sunt gresite")
        else:
            self.authenticated_user = user
        return self.cleaned_data    