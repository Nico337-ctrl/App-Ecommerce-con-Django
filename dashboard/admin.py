
from django.contrib import admin
from .models import Productos

class AdminProductos(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'cantidad', 'precio', 'estado')

admin.site.register(Productos, AdminProductos)
