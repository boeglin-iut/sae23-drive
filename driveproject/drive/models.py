
from django.db import models
from PIL import Image


class Categories(models.Model):
    nom = models.CharField(max_length=50)
    descriptif = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.nom


class Clients(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_inscription = models.DateField(blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'

    def __str__(self):
        return self.nom


class Commandes(models.Model):
    id_client = models.ForeignKey(Clients, models.CASCADE, db_column='id_client', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'commandes'
    def __str__(self):
        return self.id_client.nom



class ListeProduit(models.Model):
    id_commande = models.ForeignKey(Commandes,models.CASCADE, db_column='id_commande', blank=True, null=True)
    id_produit = models.ForeignKey('Produits', models.CASCADE, db_column='id_produit', blank=True, null=True)
    quantite = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liste_produit'


class Produits(models.Model):
    nom = models.CharField(max_length=50)
    date_de_peremption = models.DateField(blank=True, null=True)
    photo = models.ImageField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            img = Image.open(self.photo.path)
            max_size = (50, 50)
            img.thumbnail(max_size)
            img.save(self.photo.path)

    marque = models.CharField(max_length=100, blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    id_categorie = models.ForeignKey(Categories, models.CASCADE, db_column='id_categorie', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'produits'



