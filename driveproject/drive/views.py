from django.shortcuts import render

def index(request):
    return render(request, 'drive/index.html')

def categories(request):
    return render(request, 'drive/categories/categories.html')

def categories_add(request):
    return render(request, 'drive/categories/categories_add.html')

def categories_edit(request, id):
    return render(request, 'drive/categories/categories_edit.html')

def categories_delete(request, id):
    return render(request, 'drive/categories/categories_delete.html')

def clients(request):
    return render(request, 'drive/clients/commandes.html')

def clients_add(request):
    return render(request, 'drive/clients/clients_add.html')

def clients_edit(request, id):
    return render(request, 'drive/clients/clients_edit.html')

def clients_delete(request, id):
    return render(request, 'drive/clients/clients_delete.html')

def commandes(request):
    return render(request, 'drive/commandes/commandes.html')

def commandes_add(request):
    return render(request, 'drive/commandes/commandes_add.html')

def commandes_edit(request, id):
    return render(request, 'drive/commandes/commandes_edit.html')

def commandes_delete(request, id):
    return render(request, 'drive/commandes/commandes_delete.html')

def liste_produits(request):
    return render(request, 'drive/liste_produits/liste_produits.html')

def liste_produits_add(request):
    return render(request, 'drive/liste_produits/liste_produits_add.html')

def liste_produits_edit(request, id):
    return render(request, 'drive/liste_produits/liste_produits_edit.html')

def liste_produits_delete(request, id):
    return render(request, 'drive/liste_produits/liste_produits_delete.html')

def produits(request):
    return render(request, 'drive/produits/produits.html')

def produits_add(request):
    return render(request, 'drive/produits/produits_add.html')

def produits_edit(request, id):
    return render(request, 'drive/produits/produits_edit.html')

def produits_delete(request, id):
    return render(request, 'drive/produits/produits_delete.html')