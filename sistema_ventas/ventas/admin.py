from django.contrib import admin
from .models import (
    Producto,
    Proveedor,
    DetalleProducto,
    Cliente,
    Etiqueta,
    Ventas,
    Categoria,
    Profile
    )

admin.site.register(Profile)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(DetalleProducto)
admin.site.register(Cliente)
admin.site.register(Etiqueta)
admin.site.register(Ventas)
admin.site.register(Categoria)