from django.shortcuts import render
from .models import Producto
from .models import Producto, Categoria
from django.shortcuts import render, get_object_or_404
from django.urls import path
from . import views
from django.db.models import Prefetch


def lista_productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/lista_productos.html', context)



def detalle_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug, disponible=True)
    context = {'producto': producto}
    return render(request, 'tienda/detalle_producto.html', context)

def index(request):
    categorias = Categoria.objects.prefetch_related('producto_set').all()
    productos_destacados = Producto.objects.filter(disponible=True)[:8]
    context = {
        'categorias': categorias,
        'productos_destacados': productos_destacados,
    }
    return render(request, 'tienda/index.html', context)


urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
]