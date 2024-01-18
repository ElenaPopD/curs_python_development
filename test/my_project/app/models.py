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