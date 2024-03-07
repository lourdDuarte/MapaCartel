from django.shortcuts import render, redirect
from proveedor.models import Proveedor
from .forms import PrecioProveedorForm
from django.contrib import messages
# Create your views here.
def view_listado(request):
    pass

def add_precio(request):
    proveedores = Proveedor.objects.all()
    context = {'provedores':proveedores}
    if request.method == 'POST':
        form = PrecioProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Precio cargada con exito!')  # Define el mensaje de éxito
            redirect()
    return render(request,'cargar_precio.html', context)