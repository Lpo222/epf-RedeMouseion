from bottle import Bottle, request, template, redirect
from services.publication_service import PublicationService
from models.user import UserModel, Pesquisador
from config import Config

publication_routes = Bottle()
publication_service = PublicationService()
user_model = UserModel()

def get_current_user():
    user_id = request.get_cookie("user_id", secret=Config.SECRET_KEY)
    if user_id:
        return user_model.get_by_id(int(user_id))
    else:
        return None

@publication_routes.get('/publications')
def list_publications():
    publications = publication_service.get_all()
    return template('publications', publications=publications)

@publication_routes.get('/publications/add')
def show_add_form():

    current_user = get_current_user()

    if current_user and isinstance(current_user, Pesquisador):
        return template('publication_form')
    else:
        return redirect('/login')

@publication_routes.post('/publications/add')
def add_publication():

    current_user = get_current_user()

    if not (current_user and isinstance(current_user, Pesquisador)):
        return redirect('/login')
    
    publication_service.save(author_id=current_user.id)
    redirect('/publications')