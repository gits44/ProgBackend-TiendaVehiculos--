from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def vehiculos(request):
    return render(request, 'Vehiculos.html')

def sucursal(request):
    return render(request, 'Sucursal.html')

def nosotros(request):
    return render(request, 'Nosotros.html')