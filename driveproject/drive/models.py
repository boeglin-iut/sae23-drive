# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorie(models.Model):
    id_cat = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    descriptif = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Clients(models.Model):
    id_client = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    date_inscription = models.DateField(blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Commandes(models.Model):
    id_commande = models.IntegerField(primary_key=True)
    id_client = models.ForeignKey(Clients, models.DO_NOTHING, db_column='id_client', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commandes'


class ListeProduits(models.Model):
    id_liste = models.IntegerField(primary_key=True)
    quantite = models.IntegerField(blank=True, null=True)
    id_produit = models.ForeignKey('Produit', models.DO_NOTHING, db_column='id_produit', blank=True, null=True)
    id_commande = models.ForeignKey(Commandes, models.DO_NOTHING, db_column='id_commande', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liste_produits'


class Produit(models.Model):
    id_produit = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    date_de_peremption = models.DateField(blank=True, null=True)
    marque = models.CharField(max_length=50, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_categorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='id_categorie', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produits'
