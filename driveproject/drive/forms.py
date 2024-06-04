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
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-group'}),
            'descriptif': forms.Textarea(attrs={'class': 'form-group'}),
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
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-group'}),
            'prenom': forms.TextInput(attrs={'class': 'form-group'}),
            'adresse': forms.Textarea(attrs={'class': 'form-group'}),
        }

class CommandesForm(ModelForm):
    class Meta:
        model = models.Commandes
        fields = ['id_client']
        labels = {
            'id_client': _('Client'),
        }
        widgets = {
            'id_client': forms.Select(attrs={'class': 'form-group'}),
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
            'nom': forms.TextInput(attrs={'class': 'form-group'}),
            'date_de_peremption': forms.DateInput(attrs={'class': 'form-group', 'type': 'date'}),
            'photo': forms.FileInput(attrs={'class': 'form-group'}),
            'marque': forms.TextInput(attrs={'class': 'form-group'}),
            'prix': forms.NumberInput(attrs={'class': 'form-group'}),
            'id_categorie': forms.Select(attrs={'class': 'form-group'}),
        }

class ListeProduitForm(ModelForm):
    class Meta:
        model = models.ListeProduit
        fields = ['id_commande', 'quantite']
        labels = {
            'id_commande': _('Commande'),
            'quantite': _('Quantité'),
        }
        widgets = {
            'id_commande': forms.Select(attrs={'class': 'form-group'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-group'}),
        }

class ListeProduitEditForm(ModelForm):
    class Meta:
        model = models.ListeProduit
        fields = ['quantite']
        labels = {
            'quantite': _('Quantité'),
        }
        widgets = {
            'quantite': forms.NumberInput(attrs={'class': 'form-group'}),
        }