% rebase('layout', title='Publicações')
<section>
    <h1>Últimas Publicações</h1>
    <a href="/publications/add" class="btn-submit">Nova Publicação</a>
    <hr>
    % for pub in publications:
        <article>
            <h2>{{pub.title}}</h2>
            <p>{{pub.content}}</p>
            <small>Autor ID: {{pub.author_id}} | Data: {{pub.created_at}}</small>
        </article>
        <hr>
    % end
</section>