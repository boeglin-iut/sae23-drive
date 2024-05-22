from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),

    path('categories/', views.categories),
    path('categories/<int:id>/', views.categories),
    path('categories/add/', views.categories_add),
    path('categories/edit/<int:id>/', views.categories_edit),
    path('categories/delete/<int:id>/', views.categories_delete),

    path('clients/', views.clients),
    path('clients/<int:id>/', views.clients),
    path('clients/add/', views.clients_add),
    path('clients/edit/<int:id>/', views.clients_edit),
    path('clients/delete/<int:id>/', views.clients_delete),

    path('commandes/', views.commandes),
    path('commandes/<int:id>/', views.commandes_id),
    path('commandes/add/', views.commandes_add),
    path('commandes/edit/<int:id>/', views.commandes_edit),
    path('commandes/delete/<int:id>/', views.commandes_delete),

    path('liste_produits/<int:id>', views.liste_produits),
    path('liste_produits/add/<int:id_prod>/<int:id_com>/<int:quantite>/', views.liste_produits_add),
    path('liste_produits/edit/<int:id>/<int:new_quantite>/', views.liste_produits_edit),
    path('liste_produits/delete/<int:id>/', views.liste_produits_delete),

    path('produits/', views.produits),
    path('produits/<int:id>/', views.produits),
    path('produits/add/', views.produits_add),
    path('produits/edit/<int:id>/', views.produits_edit),
    path('produits/delete/<int:id>/', views.produits_delete),
]
