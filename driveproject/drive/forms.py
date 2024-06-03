from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CategoriesForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = ['nom', 'descriptif']
        labels = {
            'nom': _('Nom'),
            'descriptif': _('Descriptif'),
        }

class ClientsForm(ModelForm):
    class Meta:
        model = models.Clients
        fields = ['nom', 'prenom', 'adresse']
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'adresse': _('Adresse'),
        }

class CommandesForm(ModelForm):
    class Meta:
        model = models.Commandes
        fields = ['id_client']
        labels = {
            'id_client': _('Client'),
        }

class ProduitsForm(ModelForm):
    class Meta:
        model = models.Produits
        fields = ['nom', 'date_de_peremption', 'photo', 'marque', 'prix', 'id_categorie']
        labels = {
            'nom': _('Nom'),
            'date_de_peremption': _('Date de péremption'),
            'photo': _('Photo'),
            'marque': _('Marque'),
            'prix': _('Prix'),
            'id_categorie': _('Catégorie'),
        }
        widgets = {
            'date_de_peremption': forms.DateInput(attrs={'type': 'date'}),
        }

class ListeProduitForm(ModelForm):
    class Meta:
        model = models.ListeProduit
        fields = ['id_commande', 'quantite']
        labels = {
            'id_commande': _('Commande'),
            'quantite': _('Quantité'),
        }

class ListeProduitEditForm(ModelForm):
    class Meta:
        model = models.ListeProduit
        fields = ['quantite']
        labels = {
            'quantite': _('Quantité'),
        }