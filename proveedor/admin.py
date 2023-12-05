from django.contrib import admin
from proveedor.models import Proveedor
# Register your models here.



# tu_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User

class ProveedorInline(admin.StackedInline):
    model = Proveedor
    can_delete = False

class CustomUserCreationForm(UserCreationForm):
    # Puedes personalizar el formulario de usuario aquí si es necesario
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    inlines = [ProveedorInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Proveedor)