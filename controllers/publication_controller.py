from bottle import Bottle, request, template, redirect
from services.publication_service import PublicationService
from models.user import UserModel, Pesquisador

publication_routes = Bottle()
publication_service = PublicationService()
user_model = UserModel()

SIMULATED_USER_ID = 1

@publication_routes.get('/publications')
def list_publications():
    publications = publication_service.get_all()
    return template('publications', publications=publications)

@publication_routes.get('/publications/add')
def show_add_form():
    current_user = user_model.get_by_id(SIMULATED_USER_ID)
    if current_user and isinstance(current_user, Pesquisador):
        return template('publication_form')
    else:
        return "Acesso negado: você não tem permissão para criar publicações."

@publication_routes.post('/publications/add')
def add_publication():
    current_user = user_model.get_by_id(SIMULATED_USER_ID)
    if not (current_user and isinstance(current_user, Pesquisador)):
        return "Erro: Ação não permitida."
    publication_service.save(author_id=current_user.id)
    redirect('/publications')