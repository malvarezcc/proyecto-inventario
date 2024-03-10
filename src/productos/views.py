from django.shortcuts import render, HttpResponse

# Create your views here.


def  productos(request):
    return render(request, 'productos/productos.html')

