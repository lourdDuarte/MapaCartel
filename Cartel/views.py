from django.shortcuts import render, redirect, get_object_or_404, render

from django.contrib import messages
from Localidad.models import Localidad
from Cartel.models import Cartel
from proveedor.models import Proveedor
from .forms import CartelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView
import yagmail
from django.db.models import Count


# Create your views here.
class CartelTemplateView(TemplateView):
    
    template_name = "mapa.html"
    
    def get_context_data(self, **kwargs):
        
        template_name = "mapa.html"
        context = super().get_context_data(**kwargs)

        context['ubicaciones'] = Cartel.objects.all()
       
        context['localidad'] = Localidad.objects.all()

        context['proveedor'] = Proveedor.objects.all()

        return context
    

    

    

    @login_required
    def add_new_cartel(request):
        if request.method == 'POST':
            form = CartelForm(request.POST, request.FILES)
            print(form)
            if form.is_valid():
                
                form.save()
                messages.success(request, '¡Cartel cargada con exito!')  # Define el mensaje de éxito
                return redirect('formulario')
            else:
                messages.error(request, form.errors)
                form = CartelForm()
        localidad = Localidad.objects.all()
        proveedores = Proveedor.objects.all()
        
        context = {'localidad':localidad}
        context_proveedor = {'proveedores':proveedores}
        context.update(context_proveedor)
        return render(request,'nuevo_cartel.html', context)

    @login_required
    def listado_cartel(request):
        user = request.user.id
        cartel = Cartel.objects.filter(usuario=request.user.id)
        context = {'carteles':cartel}
        
        return render(request,'listado_cartel.html', context)
    
    def actualizar_cartel(request,pk):
        cartel = Cartel.objects.get(id=pk)
        form = CartelForm(instance=cartel)
        if request.method == 'POST':
             form = CartelForm(request.POST, request.FILES,instance=cartel)
             form.save()
             return redirect('listado')
        
        context = {'form':form}
        return render (request,'actualizar_cartel.html',context)

    
    def solicitud_usuario(request):
        destinario = 'lourdes123duarte@gmail.com'
        password = 'badspsaurjkgkxvj'
        email = 'lourdes123duarte@gmail.com'
        
        if request.method == 'POST':

                nombre = request.POST['nombre_dependencia']
                correo = request.POST['correo']
                comentario = request.POST['comentario']
            
                if (len(nombre) and len(correo) ):
                    yag = yagmail.SMTP(user = email, password = password)

                    destinario = [destinario]

                    asunto = 'SISTEMA DE CARTELES: SOLICITUD DE NUEVO USUARIO '

                    mensaje = 'Se solicita un nuevo usuario para la dependencia: '+  nombre +'.' +'<br>Por el siguiente motivo: ' + comentario +'.' +'<br> Se adjunta el correo al cual enviar la informacion: ' + correo

                    yag.send(destinario,asunto, mensaje) 


                    messages.success(request, 'Solicitud enviada. Quede atento a su correo')  # Define el mensaje de éxito
                    return redirect('registrarse')
                else:
                    messages.error(request,'Los campos nombre y correo no pueden estar vacio')
                    return redirect('registrarse')
        
        return render(request, 'nuevo_usuario.html')

    def post(self, request, *args, **kwargs):

        localidad = request.POST.get('selectLocalidad')
        proveedor = request.POST.get('selectProveedor')
        
        data = Cartel.objects.all()
        if (localidad != '0'): 
            data = data.filter(localidad_id = localidad)
        if (proveedor != '0'):
            data = data.filter(proveedor_id = proveedor)

        
        context = self.get_context_data()
        if (localidad != '0' or proveedor != '0'):
            context['data'] = data
           
       
        
        
        return render(request, self.template_name, context)
    
    def view_dashboard(request):
        proveedores = Proveedor.objects.all()
        localidades = Localidad.objects.all()
        total_proveedores = Cartel.objects.values('localidad_id').annotate(total= Count('localidad_id'))
        context = {'proveedores':proveedores}
        context_localidad = {'localidades':localidades}
       
        context_total_prov = {'total_proveedores': total_proveedores}
        context.update(context_total_prov)

        if request.method == 'POST':
         
          id_proveedor = request.POST['id_proveedor']
          if (id_proveedor != 0):
            total_final = Cartel.objects.filter(proveedor_id = id_proveedor).values('localidad_id', 'proveedor_id').annotate(total= Count('id'))
            context_total = {'total_final':total_final}
            
            context.update(context_total)
          else:
              print("error")
          
        
       
        context.update(context_localidad)
        
        
        return render(request,'dashboard.html', context)
   
    def view_dashboard_filter(request):
        proveedores = Proveedor.objects.all()
        localidades = Localidad.objects.all()
        
        context = {'proveedores':proveedores}
        context_localidad = {'localidades':localidades}
       
        
        if request.method == 'POST':
         
          id_proveedor = request.POST['id_proveedor']
          if (id_proveedor != 0):
            total_final = Cartel.objects.filter(proveedor_id = id_proveedor).values('localidad_id', 'proveedor_id').annotate(total= Count('id'))
            context_total = {'total_final':total_final}
            
            context.update(context_total)
          else:
              print("error")
          
        
       
        context.update(context_localidad)
        
        return render(request, 'dashboard_filtros.html', context)
    

    def eliminar_cartel(request, pk):
        request = Cartel.objects.get(id=pk)
        request.delete()
        return redirect('listado')
    
    def login(request):
        
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
              
                login(request, user)
                return redirect('listado')
            else:
               
                return render(request, 'login.html', {'error': 'Invalid username and password'})


        return render(request,'login.html')
    

    def logout_view(request):
        logout(request)
        return redirect('formulario')