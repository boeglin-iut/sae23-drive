from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CategoriesForm, ClientsForm, ProduitsForm
from .models import Categories, Clients, Commandes, ListeProduit, Produits

def index(request):
    return render(request, 'drive/index.html')

def categories(request):
    Categorie = Categories.objects.all()
    return render(request, 'drive/categories/categories.html', {'Categories': Categorie})

def categories_add(request):
    if request.method == 'POST':
        catform = CategoriesForm(request.POST)
        if catform.is_valid():
            catform.save()
            return render(request, 'drive/categories/categories.html', {'Categories': Categories.objects.all()})
        else:
            return render(request, 'drive/categories/add.html', {'catform': catform})
    else:
        catform = CategoriesForm()
        return render(request, 'drive/categories/add.html', {'catform': catform})

def categories_edit(request, id):
    return render(request, 'drive/categories/categories_edit.html')

def categories_delete(request, id):
    Categorie = Categories.objects.get(id=id)
    Categorie.delete()
    #return HttpResponseRedirect('/drive/categories/')
    return render(request, 'drive/categories/delete.html')

def clients(request):
    Client = Clients.objects.all()
    return render(request, 'drive/clients/commandes.html', {'Clients': Client})

def clients_add(request):
    return render(request, 'drive/clients/add.html')

def clients_edit(request, id):
    return render(request, 'drive/clients/edit.html')

def clients_delete(request, id):
    return render(request, 'drive/clients/delete.html')

def commandes(request):
    Commande = Commandes.objects.all()
    return render(request, 'drive/commandes/commandes.html', {'Commandes': Commande})

def commandes_add(request):
    return render(request, 'drive/commandes/add.html')

def commandes_edit(request, id):
    return render(request, 'drive/commandes/edit.html')

def commandes_delete(request, id):
    return render(request, 'drive/commandes/delete.html')

def liste_produits(request):
    Liste_Produit = ListeProduit.objects.all()
    return render(request, 'drive/liste_produits/liste_produits.html', {'Liste_Produit': Liste_Produit})

def liste_produits_add(request):
    return render(request, 'drive/liste_produits/add.html')

def liste_produits_edit(request, id):
    return render(request, 'drive/liste_produits/edit.html')

def liste_produits_delete(request, id):
    return render(request, 'drive/liste_produits/delete.html')

def produits(request):
    Produit = Produits.objects.all()
    return render(request, 'drive/produits/produits.html', {'Produits': Produit})

def produits_add(request):
    if request.method == 'POST':
        prodform = ProduitsForm(request.POST, request.FILES)
        if prodform.is_valid():
            prodform.save()
            return render(request, 'drive/produits/produits.html', {'Produits': Produits.objects.all()})
        else:
            return render(request, 'drive/produits/add.html', {'prodform': prodform})
    else:
        prodform = ProduitsForm()
        return render(request, 'drive/produits/add.html', {'prodform': prodform})

def produits_edit(request, id):
    return render(request, 'drive/produits/edit.html')

def produits_delete(request, id):
    return render(request, 'drive/produits/delete.html')
