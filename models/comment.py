import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'database.db')

class Comment:
    def __init__(self, content, author_id, publication_id, id=None, created_at=None, author_name=None):
        self.id = id
        self.content = content
        self.author_id = author_id
        self.publication_id = publication_id
        self.created_at = created_at
        self.author_name = author_name

class CommentModel:
    def get_by_publication_id(self, publication_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT c.id, c.content, c.author_id, c.publication_id, c.created_at, u.name
            FROM comments c
            JOIN users u ON c.author_id = u.id
            WHERE c.publication_id = ?
            ORDER BY c.created_at ASC
        """, (publication_id,))
        rows = cursor.fetchall()
        conn.close()
        return [Comment(id=row[0], content=row[1], author_id=row[2], publication_id=row[3], created_at=row[4], author_name=row[5]) for row in rows]
    
    def add_comment(self, comment: Comment):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO comments (content, author_id, publication_id) VALUES (?, ?, ?)",
            (comment.content, comment.author_id, comment.publication_id)
        )
        conn.commit()
        conn.close()

    def get_by_id(self, comment_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT id, content, author_id, publication_id, created_at FROM comments WHERE id = ?", (comment_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Comment(id=row[0], content=row[1], author_id=row[2], publication_id=row[3], created_at=row[4])
        return None
    
    def delete_by_id(self, comment_id: int):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
        conn.commit()
        conn.close()