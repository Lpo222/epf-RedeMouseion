<%
from models.user import Admin, User
%>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mouseion - {{title or 'Início'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>

    <header class="main-header">
        <div class="header-brand">
            <h1><a href="/publications">Mouseion</a></h1>
            % if request.user:
                <span class="user-greeting">Bem vindo, {{ request.user.name }}!</span>
            % end
        </div>

        <nav class="main-nav">
            <a href="/publications">Publicações</a>

            % if request.user and isinstance(request.user, Admin):
                <a href="/users">Gerenciar Usuários</a>
                <a href="/profile">Meu Perfil</a>
                <a href="/logout">Logout</a>
            % elif request.user and isinstance(request.user, User):
                <a href="/profile">Meu Perfil</a>
                <a href="/logout">Logout</a>
            % else:
                <a href="/login">Login</a>
            % end
        </nav>
    </header>
    <hr>
    
    % if flash_message:
        <div class="flash-message {{flash_category}}">
            <p>{{flash_message}}</p>
        </div>
    % end

    <div class="container">
        {{!base}}
    </div>

    <footer>
        <p>&copy; 2025, Projeto Mouseion. Todos os direitos reservados.</p>
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>