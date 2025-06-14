# 🚗 Parking Service API

Este é um sistema de controle de estacionamento desenvolvido com **Python**, **Django**, **Docker** e **PostgreSQL**. O objetivo é oferecer um serviço robusto para gerenciamento de usuários, mensalidades e controle de pagamentos.

---

## 🔧 Tecnologias Utilizadas

- 🐍 Python 3.12+
- 🌐 Django
- 🐘 PostgreSQL
- 🐳 Docker + Docker Compose
- 🔐 JWT Authentication
- 📄 Swagger/OpenAPI para documentação da API

---

## 📦 Funcionalidades

- ✅ Cadastro e autenticação de usuários com JWT
- 🧾 Registro de mensalidades
- 📅 Controle de meses pagos
- 🔐 Endpoints protegidos por autenticação
- 📘 Documentação interativa com Swagger

---

## 🚀 Como executar o projeto

1. Clone o repositório
git clone https://github.com/AnderAlmeida123/parkingService.git
cd parkingService

3. (Opcional) Configure variáveis de ambiente
Crie um arquivo .env se necessário, com variáveis como SECRET_KEY, DB_USER, DB_PASSWORD, etc.

4. Suba a aplicação com Docker
docker-compose up --build
Acesse o sistema em:
👉 http://localhost:8000
Swagger:
👉 http://localhost:8000/swagger/

---

🔑 Autenticação
A autenticação é feita via JWT.
Após criar um usuário, obtenha um token em:
POST /api/token/
Envie o token no cabeçalho das requisições:
Authorization: Bearer <seu_token>

---
```
📂 Estrutura do Projeto
parkingService/
├── app/                     # Código da aplicação Django
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```
---

🧪 Rodando testes
Para rodar testes automatizados (caso disponíveis):
docker-compose exec web python manage.py test

---

📜 Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se livre para abrir issues ou enviar pull requests com sugestões e melhorias.

---

👤 Autor
Desenvolvido por Anderson Almeida
🔗 GitHub: @AnderAlmeida123

