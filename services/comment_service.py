from bottle import request
from models.comment import CommentModel, Comment

class CommentService:
    def __init__(self):
        self.comment_model = CommentModel()
    
    def add_comment_to_publication(self, author_id, publication_id):
        content = request.forms.get('content')
        if content: #garante que nao haja comentarios vazios
            new_comment = Comment(content=content, author_id=author_id, publication_id=publication_id)
            self.comment_model.add_comment(new_comment)
    
    def get_by_author(self, author_id):
        return self.comment_model.get_by_author_id(author_id)

    def delete_comment(self, comment_id):
        self.comment_model.delete_by_id(comment_id)