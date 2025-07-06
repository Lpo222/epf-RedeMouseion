from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService
from config import Config
from models.user import Admin
from services.publication_service import PublicationService
from services.comment_service import CommentService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.user_service = UserService()
        self.publication_service = PublicationService()
        self.comment_service = CommentService()

    def get_current_user(self):
        """Função auxiliar para pegar o usuário logado a partir do cookie."""
        user_id = request.get_cookie("user_id", secret=Config.SECRET_KEY)
        if user_id:
            from models.user import UserModel
            return UserModel().get_by_id(int(user_id))
        return None


    # Rotas User
    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/profile', method='GET', callback=self.show_profile)

    def list_users(self):
        current_user = self.get_current_user()

        if current_user and isinstance(current_user, Admin):
            users = self.user_service.get_all()
            return self.render('users', users=users)
        else:
            self.redirect('/login')


    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add")
        else:
            # POST - salvar usuário
            self.user_service.save()
            self.set_flash_message("Usuário cadastrado com sucesso!")
            self.redirect('/users')

    def show_profile(self):
        current_user = self.get_current_user()

        if not current_user:
            return self.redirect('/login')

        #Busca as publicações e comentários do usuário logado
        user_publications = self.publication_service.get_by_author(current_user.id)
        user_comments = self.comment_service.get_by_author(current_user.id)

        return self.render('profile', 
                           user=current_user, 
                           publications=user_publications, 
                           comments=user_comments)

    def edit_user(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            self.user_service.edit_user(user)
            self.redirect('/users')


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
