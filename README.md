# Vortex Core API

A RESTful API built with **Flask**, **Flask-Smorest**, **PostgreSQL**, **Redis**, **RQ**, **Mailgun**, and **Docker**.

The project includes user authentication, database migrations, background task processing, HTML email notifications, API documentation, and deployment to Render.

> **Deployment note:** The RQ background worker is implemented and tested locally, but it is **not deployed as a separate Render Background Worker** because Render requires a separate paid service for a persistent background worker.

---

## 🚀 Features

- RESTful API built with Flask
- Flask-Smorest
- Swagger / OpenAPI documentation
- PostgreSQL database
- SQLAlchemy ORM
- Flask-Migrate / Alembic migrations
- JWT authentication
- Password hashing
- Redis
- RQ background task queue
- Mailgun email integration
- HTML email templates
- Docker
- Docker Compose
- Render deployment
- Environment variable configuration

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Flask | Web framework |
| Flask-Smorest | REST API and API documentation |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM |
| Flask-Migrate | Database migrations |
| JWT | Authentication |
| Redis | Queue storage |
| RQ | Background task processing |
| Mailgun | Email delivery |
| Docker | Containerization |
| Docker Compose | Local multi-container development |
| Render | Cloud deployment |

---

## 📁 Project Structure

```text
flask_api/
│
├── models/
│   └── user.py
│
├── resources/
│   └── user.py
│
├── migrations/
│   └── versions/
│
├── templates/
│   └── email/
│       └── action.html
│
├── app.py
├── schemas.py
├── tasks.py
├── settings.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
