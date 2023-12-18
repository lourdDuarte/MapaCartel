"""
URL configuration for MapaCarteles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Cartel.views import CartelTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mapa/', CartelTemplateView.as_view(template_name="mapa.html"), name = 'mapa'),
    # path('mapa/<str:pk>/', CartelTemplateView.view_mapa_filtro, name = 'mapa'),
    path('dashboard/', CartelTemplateView.view_dashboard, name = 'dashboard'),
    path('dashboard-filter/', CartelTemplateView.view_dashboard_filter, name = 'dashboard-filter'),
    path('formulario/', CartelTemplateView.add_new_cartel, name = 'formulario'),
    path('actualizar/<str:pk>/', CartelTemplateView.actualizar_cartel, name = 'actualizar'),
    path('eliminar/<str:pk>/', CartelTemplateView.eliminar_cartel, name = 'eliminar'),
    path('listado/', CartelTemplateView.listado_cartel, name = 'listado'),
    path('login/', CartelTemplateView.login, name = 'login'),
    path('logout/', CartelTemplateView.logout_view, name = 'logout'),
    path('registrarse/', CartelTemplateView.solicitud_usuario, name = 'registrarse')
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
