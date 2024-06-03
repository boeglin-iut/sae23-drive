# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import os
from django.db import models
from django.conf import settings


class Categories(models.Model):
    nom = models.CharField(max_length=50)
    descriptif = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        managed = False
        db_table = 'categories'


class Clients(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom + ' ' + self.prenom

    class Meta:
        managed = False
        db_table = 'clients'


class Commandes(models.Model):
    id_client = models.ForeignKey(Clients, models.DO_NOTHING, db_column='id_client', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Commande n°{self.id}"

    class Meta:
        managed = False
        db_table = 'commandes'


class ListeProduit(models.Model):
    id_commande = models.ForeignKey(Commandes, models.DO_NOTHING, db_column='id_commande', blank=True, null=True)
    id_produit = models.ForeignKey('Produits', models.DO_NOTHING, db_column='id_produit', blank=True, null=True)
    quantite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liste_produit'


class Produits(models.Model):
    nom = models.CharField(max_length=50)
    date_de_peremption = models.DateField(blank=True, null=True)
    photo = models.ImageField(max_length=255, blank=True, null=True)
    marque = models.CharField(max_length=100, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_categorie = models.ForeignKey(Categories, models.DO_NOTHING, db_column='id_categorie', blank=True, null=True)

    def __str__(self):
        return self.nom

    def photo_exists(self):
        return os.path.exists(os.path.join(settings.MEDIA_ROOT, self.photo.name)) if self.photo else False

    class Meta:
        managed = False
        db_table = 'produits'
