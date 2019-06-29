from django.db import models
from django.db import models
from django.utils import timezone
import datetime
from django.utils.encoding import iri_to_uri
from django.db.utils import NotSupportedError

class Person(models.Model):
    prenom = models.CharField(max_length=30, null=True, blank=True)
    Nom = models.CharField(max_length=30, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    domicile = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    #company = models.CharField(max_length=30, null=True, blank=True)
    # genre = models.CharField(max_length=1, null=True, blank=True)
    # RDV = models.DateTimeField(auto_now_add > 7 days for create_at)

    def __str__(self):
        return self.prenom

STATUS_CHOICES = (
    ('H', 'Homme'),
    ('F', 'Femme'),
    ('E', 'Enfant'),
)

class Article(models.Model):
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    nom_article = models.CharField(max_length=40, null=True, blank=True)
    type_modele = models.ForeignKey('Person',
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)
    nombre = models.IntegerField(default=0)


    def __str__(self):
        return self.status

class Payement(models.Model):
    payement = models.ForeignKey('Article',
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE)

    prix_article = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.payement



STATUS_CHOICES = (
        ('C', 'Client'),
        ('O', 'Ouvrier'),
        ('F', 'Fournisseur'),
    )
status = models.CharField(max_length=1, choices=STATUS_CHOICES)

class Typeperson(models.Model):
    quality_person = models.ForeignKey('Person',
                                       null=True,
                                       blank=True,
                                       on_delete=models.CASCADE)

    # client = models.CharField(max_length=25, null=True, blank=True)
    # ouvrier = models.CharField(max_length=25, null=True, blank=True)
    # fournisseur = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.quality_person

class Mesure(models.Model):

    mesure_client = models.ForeignKey('Article',
                                      null=True,
                                      blank=True,
                                      on_delete=models.CASCADE)

    epaule = models.CharField(max_length=2, null=True, blank=True)
    manche = models.CharField(max_length=2, null=True, blank=True)
    taille = models.CharField(max_length=2, null=True, blank=True)
    poitrine = models.CharField(max_length=3, null=True, blank=True)
    long_boubou = models.CharField(max_length=3, null=True, blank=True)
    long_patanlon = models.CharField(max_length=3, null=True, blank=True)
    ceinture = models.CharField(max_length=3, null=True, blank=True)
    cuisse = models.CharField(max_length=3, null=True, blank=True)
    tour_manche = models.CharField(max_length=2, null=True, blank=True)
    fesse = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.mesure_client




