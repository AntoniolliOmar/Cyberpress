from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<slug:slug>/', views.detalle_producto, name='detalle_producto'),
    path('', views.index, name='index'),  # Esta línea define la URL para la página principal

]