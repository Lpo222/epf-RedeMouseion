from bottle import Bottle, request, template, redirect, response
from services.user_service import UserService
from models.user import UserModel
from config import Config
import bcrypt

auth_routes = Bottle()
user_service = UserService()
user_model = UserModel()

@auth_routes.get('/login')
def show_login_form():
    return template('login_form', error=None)

@auth_routes.post('/login')
def process_Login():
    email = request.forms.get('email')
    password = request.forms.get('password')

    #Busca o usuário pelo email
    user = user_model.get_by_email(email)

    #Verifica se o usuário existe e se a senha está correta
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password_hash):      
        #Senha correta! Cria o cookie de sessão
        response.set_cookie('user_id', str(user.id), secret=Config.SECRET_KEY)
        return redirect('/publications')
    else:
        #Falha na autenticação. Mostra o formulario novamente com uma mensagem de erro.
        error_msg = 'Email ou senha inválidos'
        return template('login_form', error=error_msg)
    
@auth_routes.get('/logout')
def logout():
    #remove o cookie da sessão
    response.delete_cookie('user_id')
    return redirect('/login')