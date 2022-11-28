from django.contrib import admin

from core.models import Autor, Categoria, Compra, Editora, ItensCompras, Livro

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)


class ItensInline(admin.TabularInline):
    model = ItensCompras


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)
