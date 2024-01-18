from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produs(models.Model):
    titlu = models.CharField(max_length=50)
    pret = models.FloatField(db_index=True)
    stoc = models.IntegerField(default=0)
    descriere = models.CharField(max_length=1024, default='No description provided', null=True, blank=True, help_text="Intoduceti o descriere")
    imagine = models.FileField(null=True, blank=True)


class Favorit(models.Model):
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)  # noqa: F821
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Question(models.Model):
    text = models.CharField(max_length=50)

class Answer(models.Model):
    value = models.CharField(max_length=10)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=15)
    addresa = models.CharField(max_length=1024)
    oras = models.CharField(max_length=50)
    cnp = models.CharField(max_length=13, null=True, blank=True)

class Curs(models.Model):
    nume = models.CharField(max_length=50)
    descriere = models.CharField(max_length=1024, default='No description provided', null=True, blank=True, help_text="Intoduceti o descriere")

    def __str__(self):
        return f"Curs{self.nume}"


class Student(models.Model):
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    email = models.EmailField()
    cursuri = models.ManyToManyField(Curs)

    
    def __str__(self):
        return f"Student {self.nume} {self.prenume}"