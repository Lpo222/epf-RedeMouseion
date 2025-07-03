import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'database.db')

class Publication:
    def __init__(self, title, content, author_id, id=None, created_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.created_at = created_at

class PublicationModel:
    def get_all(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, content, author_id, created_at FROM publications ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()
        return [Publication(id=row[0], title=row[1], content=row[2], author_id=row[3], created_at=row[4]) for row in rows]
    
    def add_publication(self, pub: Publication):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO publications (title, content, author_id) VALUES (?, ?, ?)",
            (pub.title, pub.content, pub.author_id)
        )
        conn.commit()
        conn.close()

    def get_by_id(self, pub_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, content, author_id, created_at FROM publications WHERE id = ?", (pub_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Publication(id=row[0], title=row[1], content=row[2], author_id=row[3], created_at=row[4])
        return None
    
    def delete_by_id(self, pub_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        try:
            #Deleta todas as curtidas da publicação
            cursor.execute("DELETE FROM likes WHERE publication_id = ?", (pub_id,))
            
            #Deleta todos os comentários da publicação
            cursor.execute("DELETE FROM comments WHERE publication_id = ?", (pub_id,))
            
            #Deleta a publicação
            cursor.execute("DELETE FROM publications WHERE id = ?", (pub_id,))
            
            # Confirma (salva) todas as alterações
            conn.commit()
        except sqlite3.Error as e:
            # Se ocorrer um erro, desfaz tudo
            print(f"Erro ao deletar publicação: {e}")
            conn.rollback()
        finally:
            conn.close()
    
    def get_like_count(self, pub_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM likes WHERE publication_id = ?", (pub_id,))
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
    def is_liked_by_user(self, pub_id: int, user_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM likes WHERE publication_id = ? AND user_id = ?", (pub_id, user_id))
        result = cursor.fetchone()
        conn.close()
        return result is not None
    
    def add_like(self, pub_id: int, user_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO likes (publication_id, user_id) VALUES (?, ?)", (pub_id, user_id))
        conn.commit()
        conn.close()
    
    def remove_like(self, pub_id: int, user_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM likes WHERE publication_id = ? AND user_id = ?", (pub_id, user_id))
        conn.commit()
        conn.close()