from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.publication_service import PublicationService
from models.user import UserModel, Pesquisador
from config import Config

class PublicationController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.publication_service = PublicationService()
        self.user_model = UserModel()
        self.setup_routes()

    def setup_routes(self):
        """Define as rotas."""
        self.app.route('/publications', method='GET', callback=self.list_publications)
        self.app.route('/publications/add', method='GET', callback=self.show_add_form)
        self.app.route('/publications/add', method='POST', callback=self.add_publication)

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
            self.redirect('/publications')

publication_routes = Bottle()
PublicationController(publication_routes)