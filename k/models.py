from django.db import models
from django.utils import timezone
import psycopg2


class Person(models.Model):
    prenom = models.CharField(max_length=30, null=True, blank=True)
    nom = models.CharField(max_length=30, null=True, blank=True)
    domicile = models.CharField(max_length=30, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateField()

    def __str__(self):
        return self.prenom


class Article(models.Model):
    nom_article = models.CharField(max_length=40, null=True, blank=True)
    type_modele = models.ForeignKey('Person', null=True, blank=True,on_delete=models.CASCADE)
    qte = models.IntegerField(default=1)

    def __str__(self):
        return self.nom_article


class Payement(models.Model):
    id_payement = models.ForeignKey('Article',
                                    null=True, blank=True,
                                    on_delete=models.CASCADE)

    prix_total = models.CharField(max_length=25, null=True, blank=True)
    prix_avance = models.CharField(max_length=25, null=True, blank=True)
    prix_reliquat = models.CharField(max_length=25, null=True, blank=True)
    prix_depense = models.CharField(max_length=25, null=True, blank=True)
    nature_depenses = models.CharField(max_length=150, null=True, blank=True)


def __str__(self):
    return self.id_payement


class Mesure(models.Model):
    id_mesure = models.ForeignKey('Person',
                                  null=True, blank=True,
                                  on_delete=models.CASCADE)

    coud = models.CharField(max_length=2, null=True, blank=True)
    epaule = models.CharField(max_length=2, null=True, blank=True)
    manche = models.CharField(max_length=2, null=True, blank=True)
    tour_manche = models.CharField(max_length=2, null=True, blank=True)
    taille = models.CharField(max_length=2, null=True, blank=True)
    poitrine = models.CharField(max_length=3, null=True, blank=True)
    longueur_boubou = models.CharField(max_length=3, null=True, blank=True)
    longueur_patanlon = models.CharField(max_length=3, null=True, blank=True)
    fesse = models.CharField(max_length=3, null=True, blank=True)
    ceinture = models.CharField(max_length=3, null=True, blank=True)
    cuisse = models.CharField(max_length=3, null=True, blank=True)
    patte = models.CharField(max_length=2, null=True, blank=True)

    def __str__(self):
        return str(self.id_mesure)