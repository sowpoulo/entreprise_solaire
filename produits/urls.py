# votre_application/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('produits/', views.produits, name='produits'),
    path('solutions/', views.solutions, name='solutions'),
    path('partenaires/', views.partenaires, name='partenaires'),
    path('ifamel/', views.ifamel, name='ifamel'),
    path('contact/', views.contact, name='contact'),
]
