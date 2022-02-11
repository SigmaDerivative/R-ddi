from django.db import models
# skal ha en til en relasjon med bruker til en profil
from django.contrib.auth.models import User


class Profile(models.Model):
    # en-til-en med bruker og hvis slettes, skal profil slettes
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    image = models.ImageField(default='default1.jpg')
    cellphone_number = models.CharField(max_length=24, blank=True, null=True)
    # blank = true -> kan være null, null = True, databasen setter null fra starten.
    address = models.CharField(max_length=50, blank=True, null=True)
