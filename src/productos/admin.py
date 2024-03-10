from django.contrib import admin
from .models import Category, Producto


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'precio', 'stock')
    search_fields = ('nombre', 'descripcion', 'category__nombre')
    list_filter = ('category',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Producto, ProductoAdmin)





