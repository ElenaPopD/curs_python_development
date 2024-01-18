from django.contrib import admin

# Register your models here.
from .models import Produs, Favorit

admin.site.register(Produs)
admin.site.register(Favorit)