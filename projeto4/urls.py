from django.contrib import admin                        # painel administrativo do Django
from django.urls import include, path                   # path para rotas, include para incluir outras URLs
from rest_framework.authtoken.views import obtain_auth_token  # view que devolve o token do usuário
from rest_framework.routers import DefaultRouter        # router que gera as rotas dos ViewSets

from filmes.views import FilmesViewSet, GenerosViewSet  # ViewSets registrados no router

router = DefaultRouter()
router.register(r'generos', GenerosViewSet)   # registra endpoints para generos: /api/generos/
router.register(r'filmes', FilmesViewSet)     # registra endpoints para filmes: /api/filmes/

urlpatterns = [
    path('admin/', admin.site.urls),                      # rota do Django admin
    path('api/', include(router.urls)),                    # rotas da API sob o prefixo /api/
    path('api/token/', obtain_auth_token),                 # obtenção de token via CLI
    path('api-auth/', include('rest_framework.urls')),     # login/logout da interface navegável do DRF
]
