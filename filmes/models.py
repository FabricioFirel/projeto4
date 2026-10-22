from django.db import models


class Generos(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # nome do gênero

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['nome']

    def __str__(self):
        return self.nome  # representação em string do gênero


class Filmes(models.Model):
    titulo = models.CharField(max_length=255)                      # título do filme
    descricao = models.TextField()                                 # sinopse do filme
    ano_lancamento = models.PositiveIntegerField()                 # ano de lançamento
    genero = models.ForeignKey(                                    # relacionamento com Generos
        Generos,
        on_delete=models.CASCADE,
        related_name='filmes',
    )
    duracao = models.PositiveIntegerField()                        # duração em minutos

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo  # representação em string do filme
