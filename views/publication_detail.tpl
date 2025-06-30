% rebase('layout', title=publication.title)

<article class="publication-detail">
    <h1>{{publication.title}}</h1>
    <p class="publication-content">{{publication.content}}</p>
    <small>Autor ID: {{publication.author_id}} | Data: {{publication.created_at}}</small>
</article>

<hr>

<section class="comments-section">
    <h2>Comentários</h2>
    % for comment in comments:
        <div class="comment">
            <p>{{comment.content}}</p>
            <small>Por: <strong>{{comment.author_name}}</strong> em {{comment.created_at}}</small>
        </div>
    % end

    % if request.user:
        <h3>Deixe um comentário</h3>
        <form action="/publications/{{publication.id}}/comments" method="post" class="form-container">
            <div class="form-group">
                <textarea name="content" rows="4" required></textarea>
            </div>
            <button type="submit" class="btn-submit">Comentar</button>
        </form>
    % else:
        <p><a href="/login">Faça login</a> para comentar.</p>
    % end
</section>