from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', status=200, context={
        'name': 'Teste'
    })

def about(request):
    return render(request, 'recipes/contato.html')

def contact(request):
    return HttpResponse("CONTACT")