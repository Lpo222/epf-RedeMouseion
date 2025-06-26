from bottle import request
from models.user import UserModel, User
import bcrypt

class UserService:
    def __init__(self):
        self.user_model = UserModel()


    def get_all(self):
        users = self.user_model.get_all()
        return users


    def save(self):
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        password = request.forms.get('password')
        is_researcher = request.forms.get('is_researcher')

        role = 'pesquisador' if is_researcher else 'leitor'

        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password_bytes, salt)

        new_user = User(name=name, email=email, birthdate=birthdate, password_hash=password_hash, role=role)
        self.user_model.add_user(new_user)


    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)


    def edit_user(self, user):
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')
        new_password = request.forms.get('password')

        if new_password:
            password_bytes = new_password.encode('utf-8')
            salt = bcrypt.gensalt()
            user.password_hash = bcrypt.hashpw(password_bytes, salt)

        user.name = name
        user.email = email
        user.birthdate = birthdate

        self.user_model.update_user(user)


    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)
