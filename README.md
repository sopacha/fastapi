# FastAPI Learning Project

This is a practice project built while following a course on **FastAPI** and Python API development.  
The goal is to learn how to design and build a fully functional API using Python and FastAPI, including database integration, validation, and testing.

## 📚 What I'm Learning
- Building routes in FastAPI
- Request/response models with **Pydantic**
- Database connection with **PostgreSQL** (`psycopg2`)
- CRUD operations
- Schema validation
- Error handling
- (Later) SQL, pytest testing, and CI/CD with GitHub Actions

## 🚀 Current Status
Right now, the API supports:
- Creating, reading, updating, and deleting posts
- Connecting to a PostgreSQL database

More features and improvements will be added as I progress in the course.

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
