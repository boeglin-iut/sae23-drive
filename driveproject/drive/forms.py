from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CategoriesForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = '__all__'
        labels = {
            'nom': _('Nom'),
            'descriptif': _('Descriptif'),
        }

class ClientsForm(ModelForm):
    class Meta:
        model = models.Clients
        fields = '__all__'
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prénom'),
            'adresse': _('Adresse'),
        }

class ProduitsForm(ModelForm):
    class Meta:
        model = models.Produits
        fields = '__all__'
        labels = {
            'nom': _('Nom'),
            'date_de_peremption': _('Date de péremption'),
            'photo': _('Photo'),
            'marque': _('Marque'),
            'prix': _('Prix'),
            'id_categorie': _('Catégorie'),
        }