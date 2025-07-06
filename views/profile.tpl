% rebase('layout', title='Meu Perfil')

<section class="profile-header">
    <h1>Perfil de {{user.name}}</h1>
    <p><strong>Email:</strong> {{user.email}}</p>
    <p><strong>Função:</strong> <span class="role-badge {{user.role}}">{{user.role.capitalize()}}</span></p>
</section>

<hr>

<div class="profile-content">
    <section>
        <h2>Minhas Publicações ({{len(publications)}})</h2>
        % if publications:
            <ul class="profile-list">
            % for pub in publications:
                <li><a href="/publications/{{pub.id}}">{{pub.title}}</a></li>
            % end
            </ul>
        % else:
            <p>Você ainda não fez nenhuma publicação.</p>
        % end
    </section>

    <section>
        <h2>Meus Comentários ({{len(comments)}})</h2>
        % if comments:
            <ul class="profile-list">
            % for comment in comments:
                <li>
                    "{{comment['content'][0:50] + '...' if len(comment['content']) > 50 else comment['content']}}" 
                    em <a href="/publications/{{comment['publication_id']}}">{{comment['publication_title']}}</a>
                </li>
            % end
            </ul>
        % else:
            <p>Você ainda não fez nenhum comentário.</p>
        % end
    </section>
</div>