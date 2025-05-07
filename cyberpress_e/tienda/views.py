from django.shortcuts import render
from .models import Producto



def lista_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/lista_productos.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Producto

def detalle_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug, disponible=True)
    context = {'producto': producto}
    return render(request, 'tienda/detalle_producto.html', context)


from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
]