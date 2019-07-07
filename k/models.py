from django.db import models
from django.utils import timezone
import psycopg2



class Person(models.Model):
    prenom = models.CharField(max_length=30, null=True, blank=True)
    Nom = models.CharField(max_length=30, null=True, blank=True)
    modele = models.CharField(max_length=40, null=True, blank=True)
    prix = models.CharField(max_length=12, null=True, blank=True)
    domicile = models.CharField(max_length=30, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=30, null=True, blank=True)
    #genre = models.CharField(max_length=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prenom

