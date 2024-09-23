from django.shortcuts import render

# Create your views here.
def accueil(request):
    return render(request, 'accueil.html')
def produits(request):
    return render(request, 'produits.html')

def solutions(request):
    return render(request, 'solutions.html')

def partenaires(request):
    return render(request, 'partenaires.html')

def ifamel(request):
    return render(request, 'ifamel.html')

def contact(request):
    return render(request, 'contact.html')