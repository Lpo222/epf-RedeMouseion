import sqlite3
import os

# garante que 'data' existe
os.makedirs('data', exist_ok=True)

#caminho para o banco de dados
DB_PATH = os.path.join('data', 'database.db')

#concta ao banco(cria o arquivo se ele ja nao existe)
connection = sqlite3.connect(DB_PATH)

#objeto que executa os comandos SQL
cursor = connection.cursor()

#comando que cria a tabela 'users'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        birthdate TEXT NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'leitor'
    )
''')

#comando que cria a tabela 'publications'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS publications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        author_id INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES users (id)
    )
''')

#comando que cria a tabela 'comments'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        author_id INTEGER NOT NULL,
        publication_id INTEGER NOT NULL,
        FOREIGN KEY (author_id) REFERENCES users (id),
        FOREIGN KEY (publication_id) REFERENCES publications (id)
    )
''')

#commita as alterações no banco
connection.commit()

#fecha a conexão
connection.close()

print('Banco de dados criado com sucesso!')