from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, DetalleProducto, Categoria, Proveedor, Cliente, Ventas, Etiqueta
from .forms import ProductoForm, DetalleProductoForm, CategoriaForm, ProveedorForm, ClienteForm, VentasForm, EtiquetaForm

#INICIO

def inicio(request):
    total_productos = Producto.objects.count()
    total_clientes = Cliente.objects.count()
    total_ventas = Ventas.objects.count()
    context = {
        'total_productos': total_productos,
        'total_clientes': total_clientes,
        'total_ventas': total_ventas,
    }
    return render(request, 'ventas/inicio.html', context)

#PRODUCTO

def listar_productos(request):
    productos = Producto.objects.prefetch_related('detalleproducto').all()
    return render(request, 'ventas/listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        detalle_form = DetalleProductoForm(request.POST)
        if producto_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save(commit=False)
            producto.save()
            producto_form.save_m2m()

            detalle = detalle_form.save(commit=False)
            detalle.producto = producto
            detalle.save

            return redirect('listar_productos')

    else:
        producto_form = ProductoForm()
        detalle_form = DetalleProductoForm()

    return render(request, 'ventas/agregar_producto.html', {
         'producto_form': producto_form,
         'detalle_form': detalle_form
     })

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'ventas/detalle_producto.html', {'producto': producto})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    try:
        detalle = producto.detalleproducto
    except DetalleProducto.DoesNotExist:
        detalle = None

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto)
        detalle_form = DetalleProductoForm(request.POST, instance=detalle)
        if producto_form.is_valid() and detalle_form.is_valid():
            producto = producto_form.save(commit=False)
            producto_form.save()
            producto_form.save_m2m()
            detalle = detalle_form.save(commit=False)
            detalle.producto = producto
            detalle.save()
            return redirect('listar_productos')
    else:
        producto_form = ProductoForm(instance=producto)
        detalle_form = DetalleProductoForm(instance=detalle)
    return render(request, 'ventas/editar_producto.html', {
        'producto_form': producto_form,
        'detalle_form': detalle_form
    })        

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
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
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'ventas/editar_categoria.html', {'form': form})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
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
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('listar_proveedores')
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'ventas/editar_proveedor.html', {'form': form})

def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('listar_proveedores')
    return render(request, 'ventas/eliminar_proveedor.html', {'proveedor': proveedor})

#CLIENTES

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/listar_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'ventas/agregar_cliente.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'ventas/editar_cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listar_clientes')
    return render(request, 'ventas/eliminar_cliente.html', {'cliente': cliente})

#VENTAS

def listar_ventas(request):
    ventas = Ventas.objects.all()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})

def agregar_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = VentasForm()
    return render(request, 'ventas/agregar_venta.html', {'form': form})

def editar_venta(request, pk):
    ventas = get_object_or_404(Ventas, pk=pk)
    if request.method == 'POST':
        form = VentasForm(request.POST, instance=ventas)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = VentasForm(instance=ventas)
    return render(request, 'ventas/editar_etiquetas.html', {'ventas': ventas})

#ETIQUETA

def listar_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'ventas/listar_etiquetas.html', {'etiquetas': etiquetas})

def agregar_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'ventas/agregar_etiqueta.html', {'form': form})

def editar_etiqueta(request, pk):
    etiqueta = get_object_or_404(Etiqueta, pk=pk)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('listar_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'ventas/editar_etiquetas.html', {'form': form})

def eliminar_etiqueta(request, pk):
    etiqueta = get_object_or_404(Etiqueta, pk=pk)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('listar_etiqueta')
    return render(request, 'ventas/eliminar_etiqueta.html', {'etiqueta': etiqueta})