<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Museion - {{title or 'Início'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>

    <header class="main-header">
        <div class="header-brand">
            <h1><a href="/">Museion</a></h1>
            % if request.user:
                <span class="user-greeting">Bem vindo, {{ request.user.name }}!</span>
            % end
        </div>

        <nav class="main-nav">
            <a href="/publications">Publicações</a>
            <a href="/users">Usuários</a>
            % if request.user:
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
        {{!base}}  </div>

    <footer>
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>