import sqlite3
import os
from dataclasses import dataclass, asdict
from typing import List

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'database.db')

class User:
    def __init__(self, name, email, birthdate, password_hash, role='leitor', id=None):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.password_hash = password_hash
        self.role = role



    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}' role='{self.role}')")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate']
        )


class Leitor(User):
    def __init__(self, name, email, birthdate, password_hash, id=None):
        super().__init__(name, email, birthdate, password_hash, role='leitor', id=id)

class Pesquisador(User):
    def __init__(self, name, email, birthdate, password_hash, id=None):
        super().__init__(name, email, birthdate, password_hash, role='pesquisador', id=id)
    def can_publish(self):
        return True

class UserModel:

    def __init__(self):
        self._ensure_table_exists()

    def _ensure_table_exists(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTERGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                birthdate TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    # essa funçao decide qual classe instanciar dependendo de qual a role
    def _create_user_from_row(self, row):
        role = row[5]
        if role == 'pesquisador':
            return Pesquisador(id=row[0], name=row[1], email=row[2], birthdate=row[3], password_hash=row[4])
        else:
            return Leitor(id=row[0], name=row[1], email=row[2], birthdate=row[3], password_hash=row[4])


    def get_all(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, birthdate, password_hash, role FROM users")
        rows = cursor.fetchall()
        conn.close()
        #converte todas as linhas em objetos de User
        return [User(id=row[0], name=row[1], email=row[2], birthdate=row[3], password_hash=row[4]) for row in rows]

    def get_by_id(self, user_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, birthdate, password_hash, role FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return self._create_user_from_row(row)
        return None
    
    def add_user(self, user: User):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, birthdate, password_hash, role) VALUES (?, ?, ?, ?, ?)",
            (user.name, user.email, user.birthdate, user.password_hash, user.role)
        )
        conn.commit()
        conn.close()

    def update_user(self, updated_user: User):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET name = ?, email = ?, birthdate = ?, password_hash = ? WHERE id = ?",
            (updated_user.name, updated_user.email, updated_user.birthdate, updated_user.password_hash, updated_user.id)
        )
        conn.commit()
        conn.close()

    def delete_user(self, user_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()