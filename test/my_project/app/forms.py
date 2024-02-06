from django import forms
from django.forms import ValidationError


class ContactForm(forms.Form):
    email = forms.EmailField(required=True, label="Adresa de email")
    subiect = forms.CharField()
    mesaj = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith("gmail.com"):
            raise forms.ValidationError("Email-ul trebuie sa fie de tip gmail.com")
        return email