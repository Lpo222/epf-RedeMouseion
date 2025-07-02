import sqlite3
import os
import bcrypt

# --- INFORMAÇÕES DO ADMIN ---
ADMIN_NAME = "Admin"
ADMIN_EMAIL = "admin@museion.com"
ADMIN_PASSWORD = "123" # Escolha uma senha forte
# --------------------------

DB_PATH = os.path.join('data', 'database.db')

# --- Lógica para criar o hash da senha ---
password_bytes = ADMIN_PASSWORD.encode('utf-8')
salt = bcrypt.gensalt()
password_hash = bcrypt.hashpw(password_bytes, salt)
# -----------------------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

try:
    cursor.execute(
        "INSERT INTO users (name, email, birthdate, password_hash, role) VALUES (?, ?, ?, ?, ?)",
        (ADMIN_NAME, ADMIN_EMAIL, "2025-01-01", password_hash, "admin")
    )
    conn.commit()
    print(f"Usuário Admin '{ADMIN_EMAIL}' criado com sucesso!")
except sqlite3.IntegrityError:
    print(f"Erro: O usuário Admin '{ADMIN_EMAIL}' já existe no banco de dados.")
finally:
    conn.close()