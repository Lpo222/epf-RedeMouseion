from bottle import request
from models.publication import PublicationModel, Publication

class PublicationService:
    def __init__(self):
        self.publication_model = PublicationModel()

    def get_all(self):
        return self.publication_model.get_all()

    def save(self, author_id):
        title = request.forms.get('title')
        content = request.forms.get('content')

        new_pub = Publication(title=title, content=content, author_id=author_id)
        self.publication_model.add_publication(new_pub)

    def get_by_id(self, pub_id):
        return self.publication_model.get_by_id(pub_id)
    
    def delete_publication(self, pub_id):
        self.publication_model.delete_by_id(pub_id)
    
    def toggle_like(self, pub_id, user_id):
        if self.publication_model.is_liked_by_user(pub_id, user_id):
            self.publication_model.remove_like(pub_id, user_id)
        else:
            self.publication_model.add_like(pub_id, user_id)