% rebase('layout', title='Nova Publicação')
<section class="form-section">
    <h1>Nova Publicação</h1>
    <form action="/publications/add" method="post" class="form-container">
        <div class="form-group">
            <label for="title">Título:</label>
            <input type="text" id="title" name="title" required>
        </div>
        <div class="form-group">
            <label for="content">Conteúdo:</label>
            <textarea id="content" name="content" rows="10" required></textarea>
        </div>
        <div class="form-actions">
            <button type="submit" class="btn-submit">Publicar</button>
            <a href="/publications" class="btn-cancel">Voltar</a>
        </div>
    </form>
</section>