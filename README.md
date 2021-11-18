# Projeto SQL
Projeto para a disciplina de Megadados. Desenvolvemos um microsserviço de controle de notas nas quais o usuário pode criar e editar disciplinas e notas relacionadas à essas matérias. Os dados são salvos em uma database local do MySQL. O serviço é baseado no framework FastAPI.

# Megadados
André Rocco e Beatriz Muniz
Prof. Fábio Ayres

# Rodando o programa
Antes de tudo devemos criar a Database do projeto no MySQL Workbench.

O seguinte script cria a database 'projetoSQL', que é utilizado pelo projeto:

```
CREATE SCHEMA IF NOT EXISTS 'projetoSQL';
USE 'projetoSQL';
```
Para conectar o serviço ao servidor de MySQL, é necessário criar um arquivo txt nomeado ```account.txt```, onde a primeira linha deverá conter o seu username e a segunda linha deve conter a sua senha. Certifique-se de que não hajam espaços e de que o arquivo está no formato correto.

Exemplo de como deve ser preenchido o arquivo ```account.txt```:

```
seu_username
sua_senha
```

Uma vez criados o arquivo de login e a database, rode o seguinte comando no terminal dentro do repositório do projeto para rodar o servidor do uvicorn:

```
uvicorn main:app --reload
```

Para acessar as funcionalidades do serviço, basta acessar o endereço http://127.0.0.1:8000/docs para interagir com a API.


