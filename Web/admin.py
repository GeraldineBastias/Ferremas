from django.contrib import admin
from .models import Producto_Comprado,Boleta,Carrito,Producto,Categoria,Tipo_Usuario,Usuario

# Register your models here.
admin.site.register(Tipo_Usuario)
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Boleta)
admin.site.register(Producto_Comprado)
