from django.contrib import admin
from .models import Cliente, Documento, Producto, Proceso

admin.site.register(Cliente)
admin.site.register(Documento)
admin.site.register(Producto)
admin.site.register(Proceso)
