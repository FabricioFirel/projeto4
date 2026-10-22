from django_filters.rest_framework import DjangoFilterBackend   # permite filtragem via query params
from rest_framework import viewsets                             # viewsets do DRF para CRUD automático

from .models import Filmes, Generos                             # modelos/tabelas usados nas views
from .serializers import FilmesSerializer, GenerosSerializer     # serializers dos modelos


# ViewSet para o modelo Generos - fornece endpoints list/retrieve/create/update/destroy
class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()            # queryset base usado pelo ViewSet
    serializer_class = GenerosSerializer        # serializer que define representação e validação
    filter_backends = [DjangoFilterBackend]     # habilita filtragem via django-filter
    filterset_fields = ['nome']                 # ex: /api/generos/?nome=Ficção


# ViewSet para o modelo Filmes - fornece endpoints CRUD e suporte a filtros
class FilmesViewSet(viewsets.ModelViewSet):
    queryset = Filmes.objects.all()             # queryset base para operações do ViewSet
    serializer_class = FilmesSerializer         # serializer usado para filmes
    filter_backends = [DjangoFilterBackend]     # habilita filtragem via django-filter
    # campos permitidos na query string, ex: ?genero__nome=Drama ou ?ano_lancamento=2014
    filterset_fields = ['titulo', 'genero', 'genero__nome', 'ano_lancamento', 'duracao']
