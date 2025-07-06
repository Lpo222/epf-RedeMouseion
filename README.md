# Mouseion: Uma Rede Social Acadêmica

Mouseion é uma aplicação web desenvolvida em Python com o framework Bottle. Inspirada no antigo Mouseion de Alexandria, a plataforma serve como uma rede social para pesquisadores e entusiastas de diversas áreas do conhecimento, permitindo a publicação e discussão de artigos e pesquisas em um ambiente moderado.

## Funcionalidades Principais

* **Sistema de Usuários com Níveis de Permissão:**
    * **Leitor:** Pode navegar pelas publicações, ler, curtir e comentar.
    * **Pesquisador:** Tem todas as permissões de um Leitor e, adicionalmente, pode criar novas publicações.
    * **Admin:** Usuário com poder de moderação, capaz de apagar qualquer publicação ou comentário na plataforma.

* **Autenticação Segura:** Sistema completo de cadastro, login e logout, com armazenamento seguro de senhas utilizando hashing com a biblioteca `bcrypt`.

* **Publicações, Comentários e Curtidas:**
    * Criação e listagem de publicações.
    * Sistema de comentários aninhados em cada publicação.
    * Funcionalidade de "Curtir" e "Descurtir", demonstrando um relacionamento Muitos-para-Muitos(N - N).

* **Página de Perfil Pessoal:** Cada usuário logado possui uma página de perfil onde pode visualizar um resumo de todas as suas contribuições (publicações e comentários).

---

    DIAGRAMA DE CLASSES

```

## Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes do Python)

### Passos para Instalação
1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/desktop/desktop/issues/18661](https://github.com/desktop/desktop/issues/18661)
    cd nome-da-pasta-do-projeto
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # No Windows
    python -m venv venv
    .\\venv\\Scripts\\activate

    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicialize o banco de dados:**
    Este comando criará o arquivo `database.db`.
    ```bash
    python init_db.py
    ```

5.  **(Opcional) Crie um usuário Administrador(Escolha Nome e Senha no arquivo `create_admin.py`):**
    ```bash
    python create_admin.py
    ```

6.  **Execute a aplicação:**
    ```bash
    python main.py
    ```
    A aplicação estará disponível em `http://localhost:8080`.

---

## 🧠 Autores e Licença

### Template Original

Este projeto foi desenvolvido a partir de um template didático para a disciplina de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this). A licença do template original permite reutilizar, modificar e compartilhar livremente.

### Projeto "Mouseion"

* **Autor:** Leonardo Póvoa Ortegal
* **Desenvolvimento:** 2025
* **Contexto:** Projeto final da disciplina de Orientação a Objetos - 2025.1.
