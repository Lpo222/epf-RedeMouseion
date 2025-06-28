% rebase ('layout', title='Login')

<section class="form-section">
    <h1>Login</h1>

    % if error:
        <div class="error-message">{{error}}</div>
    % end 

    <form action="/login" method="post" class="form-container">
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <div class="form-actions">
            <button type="submit" class="btn-submit">Entrar</button>
        </div>
    </form>
    <div class="form-footer">
        <p>Não tem uma conta? <a href="/users/add">Cadastre-se</a></p>
    </div>
</section>