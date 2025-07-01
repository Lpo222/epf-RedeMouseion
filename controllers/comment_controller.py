from bottle import Bottle, request, redirect
from services.comment_service import CommentService
from config import Config
from .base_controller import BaseController

comment_routes = Bottle()
comment_service = CommentService()

def get_current_user_id():
    """Funçao auxiliar para pegar o ID do usuario logado."""
    return request.get_cookie("user_id", secret=Config.SECRET_KEY)

@comment_routes.post('/publications/<pub_id:int>/comments')
def add_comment(self, pub_id):
    author_id = get_current_user_id()
    if not author_id:
        return redirect('/login')

    comment_service.add_comment_to_publication(publication_id=pub_id, author_id=int(author_id))
    return redirect(f'/publications/{pub_id}')