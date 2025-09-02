# FastAPI Blog API

A fully functional backend API built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**, developed as part of a comprehensive FastAPI course.  
This project implements a complete CRUD blog system with authentication, voting, database migrations, and a full test suite.

---

## 🚀 Features
- **CRUD operations** for blog posts
- **User registration** with secure password hashing
- **JWT authentication** with OAuth2 login
- **Voting system** (like/unlike posts)
- **Query parameters** for filtering and searching
- **SQLAlchemy ORM** for database interaction
- **Alembic** for database migrations
- **CORS** support for frontend integration
- **Full test suite** with pytest, fixtures, and a dedicated test database

---

## 🛠 Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) – High-performance Python API framework
- [PostgreSQL](https://www.postgresql.org/) – Relational database
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database operations
- [Alembic](https://alembic.sqlalchemy.org/) – Database migrations
- [Pytest](https://docs.pytest.org/) – Automated testing framework
- [Uvicorn](https://www.uvicorn.org/) – ASGI server

---

## 🛠 Running the Project Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/sopacha/fastapi.git
   cd fastapi-learning

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload

4. Open your browser and visit:
    ```cpp
    http://127.0.0.1:8000
