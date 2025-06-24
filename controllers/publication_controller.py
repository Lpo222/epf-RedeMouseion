from bottle import Bottle, request, template, redirect
from services.publication_service import PublicationService

publication_routes = Bottle()
publication_service = PublicationService()

@publication_routes.get('/publications')
def list_publications():
    publications = publication_service.get_all()
    return template('publications', publications=publications)

@publication_routes.get('/publications/add')
def show_add_form():
    return template('publication_form')

@publication_routes.post('/publications/add')
def add_publication():
    publication_service.save()
    redirect('/publications')