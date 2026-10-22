# importarDados.py
import csv
import sqlite3

# Caminho para o banco SQLite
db_path = "db.sqlite3"

# Conecta ao banco
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Abre o CSV e insere os dados
with open("base_filmes.csv", newline="", encoding="utf-8") as csvfile:
    arquivo = csv.DictReader(csvfile)
    for linha in arquivo:
        nome_genero = linha["genero"].strip()

        # Verifica se o gênero já existe
        cursor.execute("SELECT id FROM filmes_generos WHERE nome = ?", (nome_genero,))
        resultado = cursor.fetchone()
        if resultado:
            genero_id = resultado[0]  # reutiliza o gênero existente
        else:
            cursor.execute("INSERT INTO filmes_generos (nome) VALUES (?)", (nome_genero,))
            genero_id = cursor.lastrowid  # cria novo gênero

        titulo = linha["titulo"].strip()

        # Evita duplicar o filme caso o script seja executado mais de uma vez
        cursor.execute("SELECT id FROM filmes_filmes WHERE titulo = ?", (titulo,))
        if cursor.fetchone():
            continue

        # Insere filme
        cursor.execute(
            """
            INSERT INTO filmes_filmes (titulo, descricao, ano_lancamento, genero_id, duracao)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                titulo,
                linha["descricao"].strip(),
                int(linha["ano_lancamento"]) if linha["ano_lancamento"].strip().isdigit() else None,
                genero_id,
                int(linha["duracao"]) if linha["duracao"].strip().isdigit() else None,
            ),
        )

# Salva e fecha
conn.commit()
conn.close()
print("Importação concluída com sucesso!")
