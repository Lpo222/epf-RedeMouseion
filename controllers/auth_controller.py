from bottle import Bottle, request, redirect, response
from .base_controller import BaseController
from models.user import UserModel
from config import Config
import bcrypt

class AuthController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.user_model = UserModel()
        self.setup_routes()

    def setup_routes(self):
        """Define as rotas."""
        self.app.route('/login', method='GET', callback=self.show_login_form)
        self.app.route('/login', method='POST', callback=self.process_login)
        self.app.route('/logout', method='GET', callback=self.logout)

    def show_login_form(self):
        return self.render('login_form', error=None)

    def process_login(self):
        email = request.forms.get('email')
        password = request.forms.get('password')

        user = self.user_model.get_by_email(email)

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash):
            response.set_cookie("user_id", str(user.id), secret=Config.SECRET_KEY)
            self.redirect('/publications')
        else:
            error_msg = "Email ou senha inválidos."
            return self.render('login_form', error=error_msg)

    def logout(self):
        response.delete_cookie("user_id")
        self.redirect('/login')

auth_routes = Bottle()
AuthController(auth_routes)