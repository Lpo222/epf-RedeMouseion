<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>

    <header class="main-header">
        <h1>Minha Rede Acadêmica</h1>
        <nav class="main-nav">
            <a href="/users">Usuários</a>
            <a href="/publications">Publicações</a>

            % if request.user:
                <span class="user-greeting">Bem vindo, {{ request.user.name }}!</span>
                <a href="/logout">Logout</a>
            % else:
                <a href="/login">Login</a>
            % end
        </nav>
    </header>
    <hr>
    <div class="container">
        {{!base}}  </div>

    <footer>
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>