from rest_framework import serializers      # ferramentas do DRF para transformar a tabela em JSON

from .models import Filmes, Generos         # modelos usados pelos serializers


class GenerosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'  # expõe todos os campos do modelo Generos


class FilmesSerializer(serializers.ModelSerializer):
    # campo apenas de leitura para mostrar o nome do gênero junto do id
    genero_nome = serializers.ReadOnlyField(source='genero.nome')

    class Meta:
        model = Filmes
        fields = ['id', 'titulo', 'descricao', 'ano_lancamento', 'genero', 'genero_nome', 'duracao']
