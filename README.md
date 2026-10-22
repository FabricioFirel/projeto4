# Projeto 4 - API de Filmes (Django REST Framework)

API REST para cadastro, consulta, edição e remoção de filmes e gêneros, construída
com Django, Django REST Framework e django-filter.

Leitura (`GET`) é pública; criação, edição e remoção exigem autenticação por token.

## Estrutura do banco

| Tabela     | Campos                                                          |
|------------|-----------------------------------------------------------------|
| `Generos`  | `nome`                                                          |
| `Filmes`   | `titulo`, `descricao`, `ano_lancamento`, `genero` (FK), `duracao` |

## 1 - Preparar o ambiente

```
python -m venv venv
venv\Scripts\activate
pip install django
pip install django-filter
pip install djangorestframework
```

Ou, de uma vez só:

```
pip install -r requirements.txt
```

## 2 - Criar a estrutura do banco

```
python manage.py makemigrations
python manage.py migrate
```

## 3 - Popular o banco

O arquivo `base_filmes.csv` fica na mesma pasta do `manage.py`, junto do script:

```
python importarDados.py
```

O script cria os gêneros que ainda não existem e insere os filmes do CSV.

## 4 - Super usuário

O banco versionado neste repositório já vem com o super usuário criado:

| Usuário  | Senha  |
|----------|--------|
| `aluno1` | `1234` |

São os mesmos dados usados no exemplo de obtenção de token mais abaixo.
Para criar outro super usuário:

```
python manage.py createsuperuser
```

## 5 - Rodar o projeto

```
python manage.py runserver
```

| Endereço                      | Precisa de login?                      |
|-------------------------------|----------------------------------------|
| http://localhost:8000/api/    | Não - a leitura abre direto            |
| http://localhost:8000/admin/  | Sim - `aluno1` / `1234`                |

A leitura (`GET`) é pública por causa da permissão `IsAuthenticatedOrReadOnly`
definida no `settings.py`. Para criar, editar ou apagar pela interface navegável
do DRF, use o botão **Log in** no topo da página com o mesmo usuário.

## Endpoints

| Método                  | Rota                   | Descrição                        |
|-------------------------|------------------------|----------------------------------|
| `GET`                   | `/api/generos/`        | Lista os gêneros                 |
| `POST`                  | `/api/generos/`        | Cria um gênero                   |
| `GET/PUT/PATCH/DELETE`  | `/api/generos/{id}/`   | Consulta, edita ou remove        |
| `GET`                   | `/api/filmes/`         | Lista os filmes                  |
| `POST`                  | `/api/filmes/`         | Cria um filme                    |
| `GET/PUT/PATCH/DELETE`  | `/api/filmes/{id}/`    | Consulta, edita ou remove        |
| `POST`                  | `/api/token/`          | Obtém o token de autenticação    |

### Filtros (django-filter)

- `/api/filmes/?titulo=Parasita`
- `/api/filmes/?genero__nome=Animação`
- `/api/filmes/?ano_lancamento=1999`
- `/api/filmes/?genero=1&duracao=169`
- `/api/generos/?nome=Drama`

## Testes via CLI com curl

GET em filmes (não precisa de token):

```
curl http://localhost:8000/api/filmes/
curl http://localhost:8000/api/filmes/3/
```

Obter token de autenticação (usuário `aluno1`, senha `1234`):

```
curl.exe -X POST http://127.0.0.1:8000/api/token/ ^
  -H "Content-Type: application/json" ^
  -d "{\"username\":\"aluno1\",\"password\":\"1234\"}"
```

Adicionar um filme (CMD Windows):

```
curl.exe -X POST http://127.0.0.1:8000/api/filmes/ ^
  -H "Authorization: Token SEU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"titulo\":\"Interestelar\",\"descricao\":\"Uma exploração espacial.\",\"ano_lancamento\":2014,\"genero\":1,\"duracao\":169}"
```

Editar um filme:

```
curl.exe -X PATCH http://127.0.0.1:8000/api/filmes/3/ ^
  -H "Authorization: Token SEU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"duracao\":170}"
```

Remover um filme:

```
curl.exe -X DELETE http://127.0.0.1:8000/api/filmes/3/ ^
  -H "Authorization: Token SEU_TOKEN_AQUI"
```

Adicionar um gênero:

```
curl.exe -X POST http://127.0.0.1:8000/api/generos/ ^
  -H "Authorization: Token SEU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"nome\":\"Documentário\"}"
```
