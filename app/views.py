from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def vehiculos(request):
    return render(request, 'Vehiculos.html')

def about(request):
    return render(request, 'QuienesSomos.html')