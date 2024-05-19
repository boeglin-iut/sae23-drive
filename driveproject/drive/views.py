from django.shortcuts import render

def index(request):
    return render(request, 'drive/index.html')

def categories(request):
    return render(request, 'drive/categories/categories.html')

def categories_add(request):
    return render(request, 'drive/categories/categories_add.html')

def categories_edit(request, id):
    return render(request, 'drive/categories/categories_edit.html')

#---------------------------------------------------------------------------------------
#Commandes
def commandes(request):
    return render(request, 'drive/commandes/commandes.html')

def commandes_add(request):
    if request.method == "POST":
        form = CommandesForm(request)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/drive/produits/index.html")
    else:
        form = CommandeForm()

    return render(request, 'drive/commandes/commandes_add.html', {"form": form})

def commandes_traitement(request):
    lform = CommandesForm(request.POST)
    if lform.is_valid():
        Commande = lform.save()
        return HttpResponseRedirect('/drive/produits/index.html')
    else:
        return render(request, "drive/commandes/commandes_add.html", {"form": lform})
    return render(request, "drive/commandes/categories.html", {"Voiture": Voiture})


def commandes_edit(request, commandes_id):
    commandes = Commandes.objects.get(pk=commandes_id)
    if request.method == "POST":
        lform = CommandesForm(request.POST, instance=commandes)
        if lform.is_valid():
            lform.save()
            return HttpResponseRedirect("/drive/produits/index.html")
    else:
        lform = CommandesForm(instance=commandes)
    return render(request, "drive/commandes/commandes_edit.html", {"form": lform, "commandes_id": commandes_id})



def commandes_delete(request, commandes_id):
    commandes = Commandes.objects.get(pk=commandes_id)
    voiture.delete()
    return HttpResponseRedirect("/drive/produits/index.html")

def commandes_affiche(request, commandes_id):
    Commandes = models.Commandes.objects.get(pk=commandes_id)

    return render(request,"drive/commandes/affiche.html",{"Commandes": Commandes})


-----------------------------------------------------------------------------------------

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