# Documentação da Aplicação de Agenda de Contatos

Esta documentação apresenta uma aplicação de agenda de contatos desenvolvida usando o framework Django no padrão MVT (Model-View-Template). A aplicação permite que os usuários se cadastrem e gerenciem seus contatos por meio de um CRUD (Create, Read, Update, Delete) simples e uma interface de fácil interação.

## Requisitos

A aplicação foi desenvolvida com base em diversas bibliotecas e pacotes Python. As principais dependências utilizadas incluem:

- Django
- bcrypt
- Pillow
- python-dotenv

## Instalação

Para instalar as dependências do projeto, utilize o seguinte comando:

  ```bash
  pip install -r requirements.txt
  ```

### Configuração do Ambiente
  Crie um arquivo .env na pasta raiz do projeto.

  Configure as variáveis de ambiente necessárias, como as configurações do banco de dados e as chaves secretas.

### Uso
  Execute as migrações do banco de dados:
  ```bash
  python manage.py migrate
  ```

  Inicie o servidor de desenvolvimento:
  ```bash
  python manage.py runserver
  ```

  Acesse a aplicação em seu navegador através do seguinte link: http://localhost:8000.


### Licença
  Este projeto é disponibilizado sob a licença MIT. Executado por **Erick Staviasz** no curso Python de Otávio Miranda

### Recursos Adicionais
  Para obter mais informações sobre o framework Django e as bibliotecas utilizadas, você pode consultar a documentação oficial e os recursos adicionais:

-  Django Documentação Oficial
-  Bcrypt
-  Pillow
-  python-dotenv



  
