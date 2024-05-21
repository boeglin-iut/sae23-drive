from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CategoriesForm, ClientsForm, CommandesForm, ProduitsForm
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
    Categorie = Categories.objects.get(id=id)
    if request.method == 'POST':
        catform = CategoriesForm(request.POST, instance=Categorie)
        if catform.is_valid():
            catform.save()
            return render(request, 'drive/categories/categories.html', {'Categories': Categories.objects.all()})
        else:
            return render(request, 'drive/categories/edit.html', {'catform': catform})
    else:
        catform = CategoriesForm(instance=Categorie)
        return render(request, 'drive/categories/edit.html', {'catform': catform})

def categories_delete(request, id):
    Categorie = Categories.objects.get(id=id)
    Categorie.delete()
    return render(request, 'drive/categories/delete.html')

def clients(request):
    Client = Clients.objects.all()
    return render(request, 'drive/clients/clients.html', {'Clients': Client})

def clients_add(request):
    if request.method == 'POST':
        cliform = ClientsForm(request.POST)
        if cliform.is_valid():
            cliform.save()
            return render(request, 'drive/clients/clients.html', {'Clients': Clients.objects.all()})
        else:
            return render(request, 'drive/clients/add.html', {'cliform': cliform})
    else:
        cliform = ClientsForm()
        return render(request, 'drive/clients/add.html', {'cliform': cliform})

def clients_edit(request, id):
    if request.method == 'POST':
        Client = Clients.objects.get(id=id)
        cliform = ClientsForm(request.POST, instance=Client)
        if cliform.is_valid():
            cliform.save()
            return render(request, 'drive/clients/clients.html', {'Clients': Clients.objects.all()})
        else:
            return render(request, 'drive/clients/edit.html', {'cliform': cliform})
    else:
        Client = Clients.objects.get(id=id)
        cliform = ClientsForm(instance=Client)
        return render(request, 'drive/clients/edit.html', {'cliform': cliform})

def clients_delete(request, id):
    Client = Clients.objects.get(id=id)
    Client.delete()
    return render(request, 'drive/clients/delete.html')

def commandes(request):
    Commande = Commandes.objects.all()
    return render(request, 'drive/commandes/commandes.html', {'Commandes': Commande})

def commandes_add(request):
    # définir l'ID de la personne qui commande afin de créer une nouvelle commande
    if request.method == 'POST':
        comform = CommandesForm(request.POST)
        if comform.is_valid():
            comform.save()
            return render(request, 'drive/commandes/commandes.html', {'Commandes': Commandes.objects.all()})
        else:
            return render(request, 'drive/commandes/add.html', {'comform': comform})
    else:
        comform = CommandesForm()
        return render(request, 'drive/commandes/add.html', {'comform': comform})

def commandes_edit(request, id):
    return render(request, 'drive/commandes/edit.html')

def commandes_delete(request, id):
    return render(request, 'drive/commandes/delete.html')

def liste_produits(request):
    Liste_Produit = ListeProduit.objects.all()
    return render(request, 'drive/liste_produits/liste_produits.html', {'Produits': Liste_Produit})

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
    if request.method == 'POST':
        Produit = Produits.objects.get(id=id)
        prodform = ProduitsForm(request.POST, request.FILES, instance=Produit)
        if prodform.is_valid():
            prodform.save()
            return render(request, 'drive/produits/produits.html', {'Produits': Produits.objects.all()})
        else:
            return render(request, 'drive/produits/edit.html', {'prodform': prodform})

def produits_delete(request, id):
    Produit = Produits.objects.get(id=id)
    Produit.delete()
    return render(request, 'drive/produits/delete.html')
