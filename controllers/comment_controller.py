from bottle import Bottle
from .base_controller import BaseController
from services.comment_service import CommentService

class CommentController(BaseController):
    def __init__(self, app):
        super().__init__(app)
        self.comment_service = CommentService()
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/publications/<pub_id:int>/comments', method='POST', callback=self.add_comment)
        self.app.route('/comments/<comment_id:int>/delete', method='POST', callback=self.delete_comment)

    def add_comment(self, pub_id):
        current_user = self.get_current_user()
        if not current_user:
            return self.redirect('/login')

        self.comment_service.add_comment_to_publication(publication_id=pub_id, author_id=current_user.id)
        
        self.set_flash_message("Comentário adicionado com sucesso!")
        return self.redirect(f'/publications/{pub_id}')
    
    def delete_comment(self, comment_id):
        # Importações necessárias para esta função
        from models.user import Admin
        from models.comment import CommentModel

        current_user = self.get_current_user()

        #Verifica se o usuário é um Admin
        if not (current_user and isinstance(current_user, Admin)):
            self.set_flash_message("Acesso negado.", category='error')
            return self.redirect('/login')

        #Busca o comentário para saber para qual publicação voltar
        comment = CommentModel().get_by_id(comment_id)
        if not comment:
            self.set_flash_message("Comentário não encontrado.", category='error')
            return self.redirect('/publications')

        publication_id = comment.publication_id

        self.comment_service.delete_comment(comment_id)

        return self.redirect(f'/publications/{publication_id}')

# --- Bloco de inicialização ---
comment_routes = Bottle()
CommentController(comment_routes)