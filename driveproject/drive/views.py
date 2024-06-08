import csv
from datetime import datetime
import io

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import cm
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.contrib import messages
from reportlab.lib.pagesizes import letter

from .forms import CategoriesForm, ClientsForm, CommandesForm, ProduitsForm, ListeProduitForm, ListeProduitEditForm
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
            return HttpResponseRedirect('/drive/categories/')
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
            return HttpResponseRedirect('/drive/categories/')
            #return render(request, 'drive/categories/categories.html', {'Categories': Categories.objects.all()})
        else:
            return render(request, 'drive/categories/edit.html', {'catform': catform})
    else:
        catform = CategoriesForm(instance=Categorie)
        return render(request, 'drive/categories/edit.html', {'catform': catform})

def categories_delete(request, id):
    Categorie = Categories.objects.get(id=id)
    ListeProduit.objects.filter(id_produit__id_categorie=Categorie).delete()
    Categorie.delete()
    return render(request, 'drive/categories/delete.html')

def clients(request):
    Client = Clients.objects.all()
    return render(request, 'drive/clients/clients.html', {'Clients': Client})

def clients_add(request):
    if request.method == 'POST':
        cliform = ClientsForm(request.POST)
        if cliform.is_valid():
            form = cliform.save(commit=False)
            date = datetime.now().date()
            form.date_inscription = date
            form.save()
            return HttpResponseRedirect('/drive/clients/')
            #return render(request, 'drive/clients/clients.html', {'Clients': Clients.objects.all()})
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
            return HttpResponseRedirect('/drive/clients/')
            #return render(request, 'drive/clients/clients.html', {'Clients': Clients.objects.all()})
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
    if request.method == 'POST':
        comform = CommandesForm(request.POST)
        if comform.is_valid():
            form = comform.save(commit=False)
            date = datetime.now().date()
            form.date = date
            form.save()
            return HttpResponseRedirect('/drive/commandes/')
            #return render(request, 'drive/commandes/commandes.html', {'Commandes': Commandes.objects.all()})
        else:
            return render(request, 'drive/commandes/add.html', {'comform': comform})
    else:
        comform = CommandesForm()
        return render(request, 'drive/commandes/add.html', {'comform': comform})

def commandes_edit(request, id):
    if request.method == 'POST':
        Commande = Commandes.objects.get(id=id)
        comform = CommandesForm(request.POST, instance=Commande)
        if comform.is_valid():
            comform.save()
            return HttpResponseRedirect('/drive/commandes/')
            #return render(request, 'drive/commandes/commandes.html', {'Commandes': Commandes.objects.all()})
        else:
            return render(request, 'drive/commandes/edit.html', {'comform': comform})
    else:
        Commande = Commandes.objects.get(id=id)
        comform = CommandesForm(instance=Commande)
        return render(request, 'drive/commandes/edit.html', {'comform': comform})

def commandes_delete(request, id):
    Commande = Commandes.objects.get(id=id)
    Commande.delete()
    return render(request, 'drive/commandes/delete.html')

def liste_produits(request, id):
    Commande = Commandes.objects.get(id=id)
    Liste_Produit = ListeProduit.objects.filter(id_commande=Commande)
    return render(request, 'drive/liste_produits/liste_produits.html', {'Produits': Liste_Produit, 'Commande': Commande})

def liste_produits_add(request, id):
    produit = Produits.objects.get(id=id)
    if request.method == 'POST':
        lpform = ListeProduitForm(request.POST)
        if lpform.is_valid():
            form = lpform.save(commit=False)
            form.id_produit = produit
            form.save()
            id_commande = form.id_commande.id
            return HttpResponseRedirect('/drive/liste_produits/' + str(id_commande) + '/')
            #return render(request, 'drive/liste_produits/liste_produits.html', {'Produits': ListeProduit.objects.all()})
        else:
            return render(request, 'drive/liste_produits/add.html', {'form': lpform})
    else:
        lpform = ListeProduitForm()
        return render(request, 'drive/liste_produits/add.html', {'form': lpform})

def liste_produits_edit(request, id):
    Liste_Produit = ListeProduit.objects.get(id=id)
    if request.method == 'POST':
        lpeform = ListeProduitEditForm(request.POST, instance=Liste_Produit)
        if lpeform.is_valid():
            lpeform.save()
            id_commande = Liste_Produit.id_commande.id
            return HttpResponseRedirect('/drive/liste_produits/' + str(id_commande) + '/')
            #return render(request, 'drive/liste_produits/liste_produits.html', {'Produits': ListeProduit.objects.all()})
        else:
            return render(request, 'drive/liste_produits/edit.html', {'lpeform': lpeform})
    else:
        lpeform = ListeProduitEditForm(instance=Liste_Produit)
        return render(request, 'drive/liste_produits/edit.html', {'lpeform': lpeform})

def liste_produits_delete(request, id):
    Liste_Produit = ListeProduit.objects.get(id=id)
    id_commande = Liste_Produit.id_commande.id
    Liste_Produit.delete()
    return HttpResponseRedirect('/drive/liste_produits/' + str(id_commande) + '/')

def liste_produits_pdf(request, id):
    commande = Commandes.objects.get(id=id)
    produits = ListeProduit.objects.filter(id_commande=commande)

    try:
        buffer = io.BytesIO()

        # Créer un document PDF avec des marges de 2,5 cm
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=2.5 * cm, leftMargin=2.5 * cm, topMargin=2.5 * cm, bottomMargin=2.5 * cm)

        # Préparer les données pour le tableau
        data = [["Produit", "Quantité", "Prix unitaire", "Prix total"]]
        total = 0
        for produit in produits:
            try:
                prix_total = produit.quantite * produit.id_produit.prix
            except:
                prix_total = 0
            total += prix_total
            try:
                data.append([produit.id_produit.nom, str(produit.quantite), str(produit.id_produit.prix), str(prix_total)])
            except:
                messages.error(request, "Erreur lors de la génération du PDF : un produit contient des informations manquantes.")
                return HttpResponseRedirect('/drive/commandes/')
        data.append(["TOTAL", "", "", str(total)])

        # Calculer la largeur totale du tableau
        table_width = letter[0] - 2.5 * cm * 2  # largeur de la page - marges

        # Définir la largeur de chaque colonne en fonction de la largeur totale du tableau
        col_widths = (table_width / 4,) * 4  # diviser la largeur totale par le nombre de colonnes

        # Créer un tableau avec les largeurs de colonnes définies
        table = Table(data, colWidths=col_widths)

        # Ajouter des styles au tableau
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),

            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -2), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.darkgrey),

            # Fusionner les cellules pour "Total"
            ('SPAN', (0, -1), (2, -1)),

            # Mettre en majuscule et en gras la cellule "Total"
            ('TEXTCOLOR', (0, -1), (0, -1), colors.black),
            ('FONTNAME', (0, -1), (0, -1), 'Helvetica-Bold'),

            # Mettre en gras la somme
            ('TEXTCOLOR', (3, -1), (3, -1), colors.black),
            ('FONTNAME', (3, -1), (3, -1), 'Helvetica-Bold'),
        ])
        table.setStyle(style)

        # Ajouter le titre et le tableau au document PDF
        elements = []
        styles = getSampleStyleSheet()
        title = Paragraph("Bon de commande", styles['Title'])
        elements.append(title)
        elements.append(Spacer(1, 12))
        elements.append(table)
        doc.build(elements)

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='facture.pdf')
    except Exception as e:
        messages.error(request, f"Erreur lors de la génération du PDF : {e}")
        return HttpResponseRedirect('/drive/commandes/')

def produits(request):
    Produit = Produits.objects.all()
    return render(request, 'drive/produits/produits.html', {'Produits': Produit})

def produits_add(request):
    if request.method == 'POST':
        prodform = ProduitsForm(request.POST, request.FILES)
        if prodform.is_valid():
            prodform.save()
            return HttpResponseRedirect('/drive/produits/')
            #return render(request, 'drive/produits/produits.html', {'Produits': Produits.objects.all()})
        else:
            return render(request, 'drive/produits/add.html', {'prodform': prodform})
    else:
        prodform = ProduitsForm()
        return render(request, 'drive/produits/add.html', {'prodform': prodform})

def produits_import(request):
    if request.method == 'POST':
        if 'csvfile' not in request.FILES:
            messages.error(request, "Aucun fichier CSV n'a été téléchargé.")
            return HttpResponseRedirect('/drive/produits/import/')

        csvfile = request.FILES['csvfile']
        reader = csv.reader(csvfile.read().decode('utf-8').splitlines())
        next(reader)
        for row in reader:
            id_categorie_id = row[4]
            try:
                categorie = Categories.objects.get(id=id_categorie_id)
            except Categories.DoesNotExist:
                messages.error(request, "La catégorie n'existe pas ou n'existe plus.")
                return HttpResponseRedirect('/drive/produits/import/')
            _, created = Produits.objects.get_or_create(
                nom=row[0],
                date_de_peremption=row[1],
                marque=row[2],
                prix=row[3],
                id_categorie=categorie
            )
        return HttpResponseRedirect('/drive/produits/')
    else:
        return render(request, 'drive/produits/import.html')


def produits_edit(request, id):
    if request.method == 'POST':
        Produit = Produits.objects.get(id=id)
        prodform = ProduitsForm(request.POST, request.FILES, instance=Produit)
        if prodform.is_valid():
            prodform.save()
            return HttpResponseRedirect('/drive/produits/')
            #return render(request, 'drive/produits/produits.html', {'Produits': Produits.objects.all()})
        else:
            return render(request, 'drive/produits/edit.html', {'prodform': prodform})
    else:
        Produit = Produits.objects.get(id=id)
        prodform = ProduitsForm(instance=Produit)
        return render(request, 'drive/produits/edit.html', {'prodform': prodform})

def produits_delete(request, id):
    Produit = Produits.objects.get(id=id)
    Produit.delete()
    return render(request, 'drive/produits/delete.html')
