from django.shortcuts import render

# Create your views here.

def Inicio(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

def pago(request):
    return render(request, 'checkout.html')

def productos(request):
    return render(request, 'productos.html')

def servicios(request):
    return render(request, 'servicios.html')