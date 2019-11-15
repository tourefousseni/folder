from django.db import models
from django.utils import timezone
import psycopg2

import sys
if sys.version_info[0] >= 3:
    unicode = str


class Person(models.Model):
    # profil = models.ImageField(upload_to=None, height_field=100, width_field=100, max_length=100)
    CATEGORIE = (
        ('Client', 'CLIENT'),
        ('Ouvrier', 'OUVRIER'),
        ('Apprenti', 'APPRENTI'),
        ('Fournisseur', 'FOURNISSEUR'),
        ('Company', 'COMPANY'),
    )

    categorie = models.CharField(max_length=20, choices=CATEGORIE, default='CLIENT')

    prenom = models.CharField(max_length=30, null=True, blank=True)
    nom = models.CharField(max_length=30, null=True, blank=True)
    SEX = (
        ('H', 'Homme'),
        ('F', 'Femme'),
        ('G', 'Garçon'),
        ('f', 'Fille'),
        ('A', 'Autres'),
    )

    sex = models.CharField(max_length=200, choices=SEX, default='Homme')
    contact = models.CharField(max_length=20, null=True, blank=True)
    domicile = models.CharField(max_length=30, default='Lafiabougou')

    def __str__(self):
        return '%s %s'%(self.prenom, self.nom)

class Produit(models.Model):
    client = models.ForeignKey('Person',
                                    null=True,
                                    blank=True,
                                    on_delete=models.CASCADE)
    MODELE = (
        ('Boubou Homme', 'Boubou Homme'),
        ('Grand Boubou Homme', 'Grand Boubou Homme'),
        ('Chemise Complet', 'Chemise Complet'),
        ('Chemise Manche Long', 'Chemise Manche Long'),
        ('Chemise Manche Court', 'Chemise Manche Court'),
        ('Pagne Jupe', 'Pagne Jupe'),
        ('Pagne Simple', 'Pagne Simple'),
        ('Pagne Maniere', 'Pagne Maniere'),
        ('Patanlon', 'Patanlon'),
        ('Tenu Scolaire', 'Tenu Scolaire'),
        ('Tenu Securite', 'Tenu Securite'),
        ('AUTRES', 'AUTRES'),
    )

    modele = models.CharField(max_length=25, choices=MODELE, default='Boubou Homme')

    TISSU = (
        ('BAZIN GETZNER', 'BAZIN GETZNER'),
        ('BAZIN RICHE', 'BAZIN RICHE'),
        ('BAZIN MOYEN', 'BAZIN MOYEN'),
        ('WAX', 'WAX'),
        ('TISSU', 'TISSU'),
        ('LEGER', 'LEGER'),
        ('PERCALE', 'PERCALE'),
        ('AUTRES', 'AUTRES'),
    )

    tissu = models.CharField(max_length=25, choices=TISSU, default='BAZIN GETZNER')

    COULOIR = (
        ('BLANC', 'BLANC'),
        ('ROUGE SANG', 'ROUGE SANG'),
        ('BLEU', 'BLEU'),
        ('ORANGE', 'ORANGE'),
        ('ROSE', 'ROSE'),
        ('VERT', 'VERT'),
        ('GRIS', 'GRIS'),
        ('GRIS CLAIR', 'GRIS CLAIR'),
        ('VIOLET', 'VIOLET'),
        ('MARON', 'MARON'),
        ('MARON CLAIR', 'MARON CLAIR'),
        ('TURGUOISE', 'TURGUOISE'),
        ('JAUNE', 'JAUNE'),
        ('JAUNE CLAIR', 'JAUNE CLAIR'),
        ('NOIR', 'NOIR'),
        ('BAGA', 'BAGA'),
        ('BAGA CLAIR', 'BAGA CLAIR'),
        ('DEUX TONS', 'DEUX TONS'),
    )

    couloir = models.CharField(max_length=25, choices=COULOIR, default='BLANC')

    METRAGE = (
        (1, 'UN'),
        (2, 'DEUX'),
        (3, 'TROIS'),
        (4, 'QUATRE'),
        (5, 'CINQ'),
        (6, 'SIX'),
        (7, 'SEPT'),
        (8, 'HUIT'),
        (9, 'NEUF'),
        (10, 'DIX'),
    )

    metrage = models.IntegerField(choices=METRAGE,)

# profil = models.ImageField(upload_to=None, height_field=100, width_field=100, max_length=100)

    def __str__(self):
        return '%s %s %s'%(self.client, self.modele, self.tissu)

#
# class Depense(models.Model):
#     depense_payment = models.ForeignKey('Modele',
#                                     null=True, blank=True,
#                                     on_delete=models.CASCADE)
#
#     materiels = models.CharField.primary_key=True
#     magasin = models.CharField(max_length=10, null=True, blank=True)
#     electricite = models.CharField(max_length=10, null=True, blank=True)
#     consommable = models.CharField(max_length=10, null=True, blank=True)
#     autres = models.CharField(max_length=10, null=True, blank=True)
#
#     def __str__(self):
#         return self.depense_payment
#  mesure_titulaire = models.ManyToManyField('Mesure')

class Mesure(models.Model):
    mesure_client = models.ForeignKey('Person',
                               on_delete=models.CASCADE)
    coud = models.PositiveSmallIntegerField(null=True, blank=True)
    epaule = models.PositiveSmallIntegerField(null=True, blank=True)
    manche = models.PositiveSmallIntegerField(null=True, blank=True)
    tour_manche = models.PositiveSmallIntegerField(null=True, blank=True)
    taille = models.PositiveSmallIntegerField(null=True, blank=True)
    poitrine = models.PositiveSmallIntegerField(null=True, blank=True)
    longueur_boubou = models.PositiveSmallIntegerField(null=True, blank=True)
    longueur_patanlon = models.PositiveSmallIntegerField(null=True, blank=True)
    fesse = models.PositiveSmallIntegerField(null=True, blank=True)
    ceinture = models.PositiveSmallIntegerField(null=True, blank=True)
    cuisse = models.PositiveSmallIntegerField(null=True, blank=True)
    patte = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return unicode(self.mesure_client)

# class Command_Content(models.Model):
#     produit_content = models.ManyToManyField('self',  blank=True, through="Produit")
#     commands = models.ManyToManyField('self',  blank=True, through="Command")
#     prix_unitaire = models.PositiveIntegerField()
#     quantite = models.PositiveSmallIntegerField(default=1)
#     commentaire = models.TextField(max_length=250, null=True, blank=True)
#
#     def __str__(self):
#         return '%s %s %s'%(self.produit_content, self.prix_unitaire, self.commentaire)

class Command(models.Model):
    titulaire_command = models.ManyToManyField('self', blank=True)
    prix_unitaire = models.PositiveIntegerField()
    # modele_choisir = models.ManyToManyField('Produit')
    quantite = models.PositiveSmallIntegerField(default=1)
    commentaire = models.TextField(max_length=250, null=True, blank=True)
    reception = models.DateField()
    rendez_vous = models.DateField()

    def __str__(self):
        return '%s'%(self.titulaire_command)



class Payement(models.Model):
        persons = models.ForeignKey('Person', on_delete=models.DO_NOTHING)
        avance = models.PositiveIntegerField()
        commands = models.ForeignKey('Command',  on_delete=models.CASCADE)
        montant_total = models.PositiveIntegerField(null=True, blank=True)
        date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return '%s %s %s'%(self.persons, self.avance, self.montant_total)
