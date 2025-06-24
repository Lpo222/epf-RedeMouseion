from bottle import request
from models.publication import PublicationModel, Publication

class PublicationService:
    def __init__(self):
        self.publication_model = PublicationModel()

    def get_all(self):
        return self.publication_model.get_all()

    def save(self):
        title = request.forms.get('title')
        content = request.forms.get('content')

        # Substituir pelo ID do usuário logado quando o login for implementado.
        # Por enquanto, o autor é sempre o usuário com ID 1.
        author_id = 1

        new_pub = Publication(title=title, content=content, author_id=author_id)
        self.publication_model.add_publication(new_pub)