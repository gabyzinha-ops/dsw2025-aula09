from django.contrib import admin
from . import models

# Register your models here.
class AutoresAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'quantidade_posts',)

    def quantidade_posts(self, obj):
        return obj.receitas.count()


@admin.register(models.Ingredientes)
class IngredientesAdmin(admin.ModelAdmin):
    list_display = ['nome',]

    class ListaAutores(admin.TabularInline):
        model = models.Ingredientes.receitas.through
        extra = 0

    inlines = [ListaAutores,]

@admin.register(models.Receitas)
class ReceitasAdmin(admin.ModelAdmin):
    class ListaIngredientes(admin.TabularInline):
        model = models.Receitas.ingredientes.through
        extra = 0

    inlines = [ListaIngredientes,]


