**Projeto To do**

Segue abaixo algumas instruções para executar o projeto To do em seu ambiente 

**Recomendações**

Instale um ambiente virtual(virtualenv) para executar a aplicação
e a instalação de suas dependências.

Para criar sua virtualenv execute o seguinte comando:

    python3 -m venv "nome_da_virtualenv"  

**Instalação da aplicação**

Após criada sua virtualenv você pode clonar o projeto para o mesmo diretório
ao lado da sua virtualenv. (exemplo: virtualenv todo_eric)

Replique o repositório com o seguinte comando:

    git clone https://EricSzcz@bitbucket.org/EricSzcz/todo_eric.git

Caso você siga nossa recomendação neste momento é necessário ativar sua virtualenv para realizar a instalação das dependências, ative sua virtualenv executando o seguinte comando:

    source ./virtualenv/bin/activate

Após isso poderá instalar as dependências do projeto com o pipenv 

Caso não tenha o pipenv instalado use o comando
`pip3 install pipenv` para instalação

Em seguida, siga o passo a passo abaixo para instalação do To do:

1. Entre no diretório todo_eric
2. Execute o comando `pipenv install Pipfile` para que seja instalado as dependências do projeto
3. Execute o comando `python manage.py migrate` para criar os arquivos de banco de dados
4. (Opcional) Crie um usuário administrador com o comando `python manage.py createsuperuser`
5. Execute o comando  `python manage.py makemigrations` criando assim o arquivo de migration da lista de todo's
6. Execute novamente o comando `python manage.py migrate` para criar o model da lista de todo's
7. Execute o comando `python manage.py runserver` para execução da aplicação

Após execução dos passos acima a aplicaçao estará rodando em:

    localhost:8000

**Instância Docker da aplicação**

**Recomendações**

Antes de iniciar a aplicação via container Docker,
execute os passo 1 e 2 abaixo para ter certeza que a aplicação utilize o banco de dados postgres.

1. Exclua o arquivo `db.sqlite3` que se encontra na raiz do projeto
2. Exclua o arquivo de migrations que se encontra em `todo_list/migrations/*_initial.py`

**Execução**

Para executar a aplicação via docker siga os seguintes passos:

1. Execute o comando `docker-compose build` na raiz do projeto para ciar o container com a aplicação e suas dependências.
2. Execute o comando `docker-compose up` também na raiz do projeto para executar o container e subir a aplicação.

Após execução dos passos acima a aplicação estará rodando em:

    localhost:8000

