from django.shortcuts import render, redirect
from .models import Producto, Categoria, Proveedor
from .forms import ProductoForm, CategoriaForm, ProveedorForm

#INICIO
def inicio(request):
    return render(request, 'ventas/inicio.html')

#PRODUCTO
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/listar_productos.html', {'productos': productos})
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'ventas/agregar_producto.html', {'form': form})
def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ventas/editar_producto.html', {'form': form})
def eliminar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_producto')
    return render(request, 'ventas/eliminar_producto.html', {'producto': producto})

#CATEGORIA
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'ventas/listar_categorias.html', {'categorias': categorias})
def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'ventas/agregar_categoria.html', {'form': form})
def editar_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'ventas/editar_categoria.html', {'form': form})
def eliminar_categoria(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    return render(request, 'ventas/eliminar_categoria.html', {'categoria': categoria})

#PROVEEDOR
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ventas/listar_proveedores.html', {'proveedores': proveedores})
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'ventas/agregar_proveedor.html', {'form': form})
def editar_proveedor(request, pk):
    proveedor = Proveedor.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'ventas/editar_proveedor.html', {'form': form})
def eliminar_proveedor(request, pk):
    proveedor = Proveedor.objects.get(pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'ventas/eliminar_proveedor.html', {'proveedor': proveedor})