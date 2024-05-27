from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CategoriesForm, ClientsForm, CommandesForm, ProduitsForm, ListeProduitForm
from .models import Categories, Clients, Commandes, ListeProduit, Produits
import csv
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
            return HttpResponseRedirect('/drive/categories')
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
    return HttpResponseRedirect('/drive/categories')

def clients(request):
    Client = Clients.objects.all()
    return render(request, 'drive/clients/clients.html', {'Clients': Client})

def clients_add(request):
    if request.method == 'POST':
        cliform = ClientsForm(request.POST)
        if cliform.is_valid():
            cliform.save()
            return HttpResponseRedirect('/drive/clients')
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
            return HttpResponseRedirect('/drive/clients')
        else:
            return render(request, 'drive/clients/edit.html', {'cliform': cliform})
    else:
        Client = Clients.objects.get(id=id)
        cliform = ClientsForm(instance=Client)
        return render(request, 'drive/clients/edit.html', {'cliform': cliform})

def clients_delete(request, id):
    Client = Clients.objects.get(id=id)
    Client.delete()
    return HttpResponseRedirect('/drive/clients')

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
    command = Commandes.objects.get(id=id)
    if request.method == 'POST':
        form = CommandesForm(request.POST, instance=command)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/drive/commandes')
    else:
        form = CommandesForm(instance=command)
    return render(request, 'drive/commandes/edit.html', {'form': form})

def commandes_delete(request, id):
    command = Commandes.objects.get(id=id)
    command.delete()
    return HttpResponseRedirect('/drive/commandes')
def liste_produits(request, id):
    command = Commandes.objects.get(id=id)
    Liste_Produit = ListeProduit.objects.filter(id_commande=command)
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
            prodform.save()  # Corrected here
            return render(request, 'drive/produits/produits.html')
        else:
            return render(request, 'drive/produits/add.html', {'prodform': prodform})
    else:
        prodform = ProduitsForm()
        return render(request, 'drive/produits/add.html', {'prodform': prodform})

def produits_edit(request, id):
    Produit = Produits.objects.get(id=id)
    if request.method == 'POST':
        prodform = ProduitsForm(request.POST, request.FILES, instance=Produit)
        if prodform.is_valid():
            prodform.save()
            return HttpResponseRedirect("/drive/produits/")
        else:
            return render(request, 'drive/produits/edit.html', {'prodform': prodform})
    else:
        prodform = ProduitsForm(instance=Produit)
        return render(request, 'drive/produits/edit.html', {'prodform': prodform})
def produits_delete(request, id):
    Produit = Produits.objects.get(id=id)
    Produit.delete()
    return render(request, 'drive/produits/delete.html')



def import_products(request):
    if request.method == 'POST':
        csvfile = request.FILES['csvfile']
        reader = csv.reader(csvfile.read().decode('utf-8').splitlines())
        next(reader)
        for row in reader:
            _, created = Produits.objects.get_or_create(
                nom=row[0],
                date_de_peremption=row[1],
                photo=row[2],
                marque=row[3],
                prix=row[4],
                id_categorie_id=row[5]
            )
        return HttpResponseRedirect("/drive/produits/")
    return render(request, 'drive/produits/import.html')



def add_to_command(request, id):
    produit = Produits.objects.get(id=id)
    if request.method == 'POST':
        post = request.POST.copy()  # Make a mutable copy of the POST data
        post['id_produit'] = produit.id  # Set the 'id_produit' field to the product's ID
        form = ListeProduitForm(post)  # Pass the modified POST data to the form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/drive/produits/")
    else:
        form = ListeProduitForm(initial={'id_produit': produit})
    return render(request, 'drive/produits/add_to_command.html', {'form': form, 'produit': produit})