from django.shortcuts import render, redirect
from proveedor.models import Proveedor
from .models import PrecioProveedor
from .forms import PrecioProveedorForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def add_precio(request):
    proveedores = Proveedor.objects.all()
    context = {'provedores':proveedores}
    if request.method == 'POST':
        form = PrecioProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Precio cargada con exito!')  # Define el mensaje de éxito
            redirect('nuevo-precio')
        else:
            messages.error(request, form.errors)
            form = PrecioProveedorForm()

    return render(request,'cargar_precio.html', context)

@login_required
def listado_precios(request):
    
    lista_precio = PrecioProveedor.objects.all()
    context = {'lista_precio': lista_precio}

    return render(request,'listado_precios.html', context)

@login_required
def actualizar_precio(request, pk):
    precio = PrecioProveedor.objects.get(id=pk)
    form = PrecioProveedorForm(instance=precio)
    if request.method == 'POST':
        form = PrecioProveedorForm(request.POST,instance=precio)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Precio actualizado con exito!')  # Define el mensaje de éxito
            return redirect('listado-precio')
        else:
            messages.error(request, form.errors)
            form = PrecioProveedorForm()
            return render(request, 'actualizar_precio.html',{'form':form})
    
    return render(request, 'actualizar_precio.html',{'form':form})

@login_required
def eliminar_precio(request, pk):
        request = PrecioProveedor.objects.get(id=pk)
        request.delete()
        
        return redirect('listado-precio')