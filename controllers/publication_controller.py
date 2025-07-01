from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.publication_service import PublicationService
from models.user import UserModel, Pesquisador
from config import Config
from models.comment import CommentModel

class PublicationController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.publication_service = PublicationService()
        self.user_model = UserModel()
        self.comment_model = CommentModel()
        self.setup_routes()

    def setup_routes(self):
        """Define as rotas."""
        self.app.route('/publications', method='GET', callback=self.list_publications)
        self.app.route('/publications/add', method='GET', callback=self.show_add_form)
        self.app.route('/publications/add', method='POST', callback=self.add_publication)
        self.app.route('/publications/<pub_id:int>', method='GET', callback=self.show_publication_detail)
        self.app.route('/publications/<pub_id:int>/like', method='POST', callback=self.toggle_like)

    def get_current_user(self):
        """Função auxiliar para pegar o usuário logado a partir do cookie."""
        user_id = request.get_cookie("user_id", secret=Config.SECRET_KEY)
        if user_id:
            return self.user_model.get_by_id(int(user_id))
        return None

    def list_publications(self):
        publications = self.publication_service.get_all()
        return self.render('publications', publications=publications)

    def show_add_form(self):
        current_user = self.get_current_user()
        if current_user and isinstance(current_user, Pesquisador):
            return self.render('publication_form')
        else:
            self.redirect('/login')

    def add_publication(self):
        current_user = self.get_current_user()
        if not (current_user and isinstance(current_user, Pesquisador)):
            self.redirect('/login')
        else:
            self.publication_service.save(author_id=current_user.id)
            self.set_flash_message("Publicação postada com sucesso!")
            self.redirect('/publications')
    
    def show_publication_detail(self, pub_id):

        publication = self.publication_service.get_by_id(pub_id)
        comments = self.comment_model.get_by_publication_id(pub_id)
        like_count = self.publication_service.publication_model.get_like_count(pub_id)
        
        current_user = self.get_current_user()
        is_liked = False
        if current_user:
            is_liked = self.publication_service.publication_model.is_liked_by_user(pub_id, current_user.id)

        if publication:
            return self.render('publication_detail', 
                               publication=publication, 
                               comments=comments, 
                               like_count=like_count, 
                               is_liked=is_liked)
        return "Publicaçao não encontrada"
    
    def toggle_like(self, pub_id):
        current_user = self.get_current_user()
        if not current_user:
            return self.redirect('/login')
        
        self.publication_service.toggle_like(pub_id=pub_id, user_id=current_user.id)
        return self.redirect(f'/publications/{pub_id}')

publication_routes = Bottle()
PublicationController(publication_routes)