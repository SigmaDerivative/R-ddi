from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


# Klasse for dødsbo
class Estate(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    image = models.ImageField(default='default.jpg')
    users = models.ManyToManyField(User)  # n-n relasjon
    date = models.DateTimeField(auto_now_add=True)
    settled = models.BooleanField(default=False) #ferdig = true /ikke ferdig = false

    class Meta:
        ordering = ['-date']

    # Tilsvarende toString() metode i Java for å se navn istedenfor objekt1
    def __str__(self):
        return '{}'.format(self.name)
    
    def get_absolute_url(self):
        return reverse('estate_detail', args=[str(self.pk)])
    

# Klasse for eiendeler
class Belongings(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    estate = models.ForeignKey(to=Estate, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg')

    # Tilsvarende toString() metode i Java for å se navn istedenfor objekt1
    def __str__(self):
        return '{}'.format(self.name)

# Klasse for status, fordi en belongings skal kunne ha flere enn 1 status. (basert på antall personer i dødsboet)
class Status(models.Model):
    statusID = models.AutoField(primary_key=True)
    alternatives = (
        ('N/A', 'N/A'), ('Fordele', 'Fordele',), ('Donere', 'Donere',), ('Kaste', 'Kaste',),
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    belonging = models.ForeignKey(to=Belongings, on_delete=models.CASCADE)
    alternatives = models.CharField(max_length=30, choices=alternatives)
    rating = models.IntegerField(blank=True, null=True, default=0)
    
    #definere en unik nøkkel, slik at en person ikke kan sette to ulike statuser på samme gjenstand.
    class Meta:
        unique_together = (("belonging", "user"),)


class Comment(models.Model):
    belonging = models.ForeignKey(to=Belongings, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
