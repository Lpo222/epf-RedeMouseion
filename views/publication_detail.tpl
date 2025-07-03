<%
from models.user import Admin, User
%>

% rebase('layout', title=publication.title)

<article class="publication-detail">
    <h1>{{publication.title}}</h1>
    <p class="publication-content">{{publication.content}}</p>
    <small>Autor ID: {{publication.author_id}} | Data: {{publication.created_at}}</small>
</article>

<hr>
<section class="actions-section">
    <form action="/publications/{{publication.id}}/like" method="post">
        <span>{{like_count}} curtidas</span>
        % if request.user:
            <button type="submit" class="btn-like">
                % if is_liked:
                    Descurtir
                % else:
                    Curtir
                % end
            </button>
        % end
    </form>

    % if request.user and isinstance(request.user, Admin):
        <form action="/publications/{{publication.id}}/delete" method="post" onsubmit="return confirm('Tem certeza que deseja apagar esta publicação? Esta ação não pode ser desfeita.');">
            <button type="submit" class="btn-delete">Apagar Publicação</button>
        </form>
    % end

</section>

<hr>

<section class="comments-section">
    <h2>Comentários</h2>
   % for comment in comments:
        <div class="comment">
            <p>{{comment.content}}</p>
            <div class="comment-footer">
                <small>Por: <strong>{{comment.author_name}}</strong> em {{comment.created_at}}</small>

                % if request.user and isinstance(request.user, Admin):
                    <form action="/comments/{{comment.id}}/delete" method="post" onsubmit="return confirm('Tem certeza que deseja apagar este comentário?');" class="delete-comment-form">
                        <button type="submit" class="btn-delete-comment">Apagar</button>
                    </form>
                % end
            </div>
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