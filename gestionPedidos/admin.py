from re import search
from django.contrib import admin
from gestionPedidos.models import Clientes, Articulo, Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "email", "tfno")
    search_fields=("nombre", "direccion", "email", "tfno")

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidoAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulo, ArticulosAdmin)
admin.site.register(Pedidos, PedidoAdmin)