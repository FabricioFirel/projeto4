from django.contrib import admin
from rest_framework.authtoken.models import Token

from .models import Filmes, Generos


# Admin para o modelo Generos: mostra o campo 'nome' e permite busca por nome
@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']


@admin.register(Filmes)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'genero', 'ano_lancamento', 'duracao']
    search_fields = ['titulo', 'descricao', 'genero__nome']
    list_filter = ['genero', 'ano_lancamento']


admin.site.register(Token)
