from django.urls import path
from . import views
urlpatterns = [
    #INICIO
    path('', views.inicio, name='inicio'), 
    #PRODUCTO
    path('productos/', views.listar_productos, name='listar_productos'),  
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'), 
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'), 
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'), 
    #CATEGORIA
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
    #PROVEEDOR
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    #CLIENTE
    path('clientes/', views.listar_clientes, name='listar_cliente'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/eliminar/<int:pk>/', views.eliminar_cliente, name='eliminar_cliente'),
    #VENTA
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/editar/<int:pk>/', views.editar_venta, name='editar_venta'),
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    #ETIQUETA
    path('etiquetas/', views.listar_etiquetas, name='listar_etiquetas'),
    path('etiquetas/agregar/', views.agregar_etiqueta, name='agregar_etiqueta'),
    path('etiquetas/editar/<int:pk>/', views.editar_etiqueta, name='editar_etiqueta'),
    path('etiquetas/eliminar/<int:pk>/', views.eliminar_etiqueta, name='eliminar_etiqueta'),
]
