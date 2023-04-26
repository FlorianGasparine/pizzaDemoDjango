from django.db import models

class Pizza(models.Model):
    nom = models.CharField(max_length=200)
