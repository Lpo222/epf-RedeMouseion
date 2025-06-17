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
    CREATE TABLE IF NOT EXIST users (
        id INTEGER PRIMARY KEY AUTOICREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        birthdate TEXT NOT NULL
    )
''')

#commita as alterações no banco
connection.commit()

#fecha a conexão
connection.close()

print('Banco de dados criado com sucesso!')