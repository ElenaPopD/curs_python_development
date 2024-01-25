from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Produs(models.Model):
    titlu = models.CharField(max_length=50)
    pret = models.FloatField(db_index=True)
    stoc = models.IntegerField(default=0)
    descriere = models.CharField(max_length=1024, default='No description provided', null=True, blank=True, help_text="Intoduceti o descriere")
    imagine = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return f"Produs {self.titlu}"
    

class Recenzie(models.Model):
    titlu = models.CharField(max_length=50)
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    rating = models.IntegerField()
    descriere = models.CharField(max_length=1024, default='No description provided', null=True, blank=True, help_text="Intoduceti o descriere")

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
    an = models.IntegerField(default=1)

    
    def __str__(self):
        return f"Student {self.nume} {self.prenume}"

class Elev(models.Model):
    class Meta:
        unique_together = ["nume", "prenume"]


    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    an = models.IntegerField(default=1)
    cursuri = models.ManyToManyField(to=Curs, through="ElevCurs")
    
    def __str__(self):
        return f"Elev {self.nume} {self.prenume}"
    
class ElevCurs(models.Model):
    elev = models.ForeignKey(Elev, on_delete=models.CASCADE)
    curs = models.ForeignKey(Curs, on_delete=models.CASCADE)
    nota = models.IntegerField(default=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Elev {self.elev} {self.curs} {self.nota} {self.created}"  
    
class PostManager(models.Manager):

    def active(self):
        acum = now()
        return self.filter(visible_from__lte=acum).filter(models.Q(end_on__gte=acum) | models.Q(end_on__isnull=True))

class Post(models.Model):
    class Meta:
        ordering = ["-visible_from"]

    titlu = models.CharField(max_length=50)
    continut = models.CharField(max_length=1024)
    visible_from = models.DateTimeField()
    end_on = models.DateTimeField(null=True, blank=True)

    objects = PostManager()

# Post.objects.filter(visible_from__lte=acum).filter(Q(end_on__gte=acum) | Q(end_on__isnull=True))
# Post.objects.active() - same as above