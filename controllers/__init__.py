from bottle import Bottle
from controllers.user_controller import user_routes
from .publication_controller import publication_routes
from .auth_controller import auth_routes
from .comment_controller import comment_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(publication_routes)
    app.merge(auth_routes)
    app.merge(comment_routes)