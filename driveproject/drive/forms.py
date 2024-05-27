from django import forms
from django.forms import ModelForm
from .models import Categories

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

class CommandesForm(ModelForm):
    class Meta:
        model = models.Commandes
        fields = '__all__'
        labels = {
            'id_client': _('Client'),
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
            'id_categorie.nom': _('Catégorie'),
        }
from django import forms
from .models import Commandes

class AddToCommandForm(forms.Form):
    commande = forms.ModelChoiceField(queryset=Commandes.objects.all())


from django import forms
from .models import ListeProduit

from django import forms
from .models import ListeProduit

class ListeProduitForm(forms.ModelForm):
    class Meta:
        model = ListeProduit
        fields = ['id_commande', 'id_produit', 'quantite']
        widgets = {
            'id_produit': forms.HiddenInput()
        }