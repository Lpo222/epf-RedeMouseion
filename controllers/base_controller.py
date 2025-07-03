from bottle import static_file, request, response, template
from config import Config

class BaseController:
    def __init__(self, app):
        self.app = app
        self._setup_base_routes()

    def set_flash_message(self, message, category='success'):
        """Define a mensagem flash em um cookie."""
        response.set_cookie('flash_message', message, secret=Config.SECRET_KEY, max_age=2)
        response.set_cookie('flash_category', category, secret=Config.SECRET_KEY, max_age=2)

    def get_flash_message(self):
        """Lê e apaga a mensagem flash do cookie"""
        message = request.get_cookie('flash_message', secret=Config.SECRET_KEY)
        category = request.get_cookie('flash_category', secret=Config.SECRET_KEY)

        if message:
            response.delete_cookie('flash_message')
            response.delete_cookie('flash_category')

        return message, category

    def _setup_base_routes(self):
        """Configura rotas básicas comuns a todos os controllers"""
        self.app.route('/', method='GET', callback=self.home_redirect)
        self.app.route('/helper', method=['GET'], callback=self.helper)

        # Rota para arquivos estáticos (CSS, JS, imagens)
        self.app.route('/static/<filename:path>', callback=self.serve_static)


    def home_redirect(self):
        """Redireciona a rota raiz para /publications"""
        return self.redirect('/publications')


    def helper(self):
        return self.render('helper-final')


    def serve_static(self, filename):
        """Serve arquivos estáticos da pasta static/"""
        return static_file(filename, root='./static')


    def render(self, template, **context):
        """Método auxiliar para renderizar templates"""
        from bottle import template as render_template, request
        context['request'] = request
        flash_message, flash_category = self.get_flash_message()
        context['flash_message'] = flash_message
        context['flash_category'] = flash_category
        
        return render_template(template, **context)


    def redirect(self, path):
        """Método auxiliar para redirecionamento"""
        from bottle import redirect as bottle_redirect
        return bottle_redirect(path)
