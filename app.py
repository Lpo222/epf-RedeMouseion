from bottle import Bottle, request
from config import Config
from models.user import UserModel

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.user_model = UserModel()
        self._setup_hooks()

    def _setup_hooks(self):
        @self.bottle.hook('before_request')
        def setup_request():
            user_id = request.get_cookie("user_id", secret=self.config.SECRET_KEY)
            if user_id:
                # Se o cookie existir, anexa o objeto do usuário à requisição
                request.user = self.user_model.get_by_id(int(user_id))
            else:
                # Senão, anexa None
                request.user = None

    def setup_routes(self):
        from controllers import init_controllers
        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)

    def run(self):
        self.setup_routes()
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()