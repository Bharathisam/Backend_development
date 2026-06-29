# 🚀 FastAPI Stage 3 – SQLModel, SQLite & Database Migrations

## 📖 Overview

This project is the third stage of learning **FastAPI** by implementing **database integration** using **SQLModel**, **SQLite**, and **Alembic**.

The objective of this stage is to understand how to define database models, store application data in a relational database, generate migration scripts, and safely update the database schema without manually modifying database tables.

---

# 🎯 Learning Objectives

After completing this stage, you will understand:

- SQLModel ORM
- SQLite database integration
- Database Models
- Request & Response Models
- CRUD Operations
- Dependency Injection
- Database Sessions
- Alembic Migrations
- Schema Versioning
- Automatic Migration Generation

---

# 📂 Project Structure

```text
FastAPI-Stage3/
│
├── main.py                 # FastAPI application
├── models.py               # SQLModel database models
├── database.db             # SQLite database
├── pyproject.toml
├── alembic.ini             # Alembic configuration
├── README.md
├── .gitignore
│
└── alembic/
    ├── env.py
    ├── script.py.mako
    └── versions/
```

---

# ⚙️ Prerequisites

Before starting, make sure you have installed:

- Python 3.11 or later
- pip
- Virtual Environment (venv)

Check Python version:

```bash
python --version
```

---

# 🛠️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd FastAPI-Stage3
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install "fastapi[standard]"
pip install sqlmodel
pip install alembic
```

---

## 5. Run Development Server

```bash
fastapi dev
```

---

# 🌐 Application URLs

| Service | URL |
|----------|-----|
| Main Application | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |
| OpenAPI JSON | http://127.0.0.1:8000/openapi.json |

---

# 📌 Database Models

This project uses multiple models to separate the database schema from the API contract.

## HeroBase

Contains common fields shared by all models.

```python
name: str
age: int | None
```

---

## Hero

Database table model.

```python
id
name
age
secret_name
```

---

## HeroCreate

Used for creating a new hero.

```python
name
age
secret_name
```

---

## HeroPublic

Returned to API clients.

```python
id
name
age
```

> The `secret_name` field is intentionally hidden from API responses.

---

## HeroUpdate

Used for updating an existing hero.

All fields are optional.

---

# 📌 API Endpoints

## POST /heroes/

Creates a new hero.

### Request

```json
{
  "name": "Spider-Man",
  "age": 18,
  "secret_name": "Peter Parker"
}
```

### Response

```json
{
  "id": 1,
  "name": "Spider-Man",
  "age": 18
}
```

---

## GET /heroes/

Returns all heroes.

---

## GET /heroes/{hero_id}

Returns a hero by ID.

---

## PATCH /heroes/{hero_id}

Updates an existing hero.

---

## DELETE /heroes/{hero_id}

Deletes a hero.

---

# 🧪 Testing the API

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

You can:

- Create Heroes
- Retrieve Heroes
- Update Heroes
- Delete Heroes

---

# 🗄️ SQLite Database

The application automatically creates

```
database.db
```

SQLite stores all Hero records locally.

---

# 🔄 Database Migrations with Alembic

Initialize Alembic:

```bash
alembic init alembic
```

---

Generate a migration:

```bash
alembic revision --autogenerate -m "Create Hero table"
```

---

Apply the migration:

```bash
alembic upgrade head
```

---

Whenever the database model changes:

```bash
alembic revision --autogenerate -m "Add new column"
alembic upgrade head
```

This safely updates the database schema without manually editing database tables.

---

# 📚 Understanding the Code

## SQLModel

SQLModel combines SQLAlchemy and Pydantic.

It provides:

- Database ORM
- Data Validation
- Type Hints
- Automatic Serialization

---

## SQLite

SQLite is a lightweight relational database used for local development.

No additional installation is required.

---

## Dependency Injection

Database sessions are created using:

```python
Depends(get_session)
```

This automatically provides a database session for every request.

---

## Response Models

The API returns

```python
HeroPublic
```

instead of

```python
Hero
```

This prevents internal database fields such as `secret_name` from being exposed.

---

## Alembic

Alembic manages database schema changes using migration files.

Instead of manually editing tables, migrations allow database updates to be version-controlled and reproducible.

---

# 💡 Key Concepts Learned

- SQLModel
- SQLite
- ORM Models
- CRUD APIs
- Database Sessions
- Dependency Injection
- Alembic
- Database Migrations
- Request Models
- Response Models
- Schema Versioning

---

# 🛠️ Technologies Used

| Technology | Version |
|------------|----------|
| Python | 3.11+ |
| FastAPI | Latest |
| SQLModel | Latest |
| SQLAlchemy | 2.x |
| SQLite | Latest |
| Alembic | Latest |
| Uvicorn | Latest |

---

# 📈 Learning Outcomes

By completing this stage, you can:

- ✅ Create database tables using SQLModel
- ✅ Store application data in SQLite
- ✅ Build CRUD APIs
- ✅ Separate Database Models from API Models
- ✅ Generate Alembic migration files
- ✅ Apply database migrations
- ✅ Safely modify database schemas
- ✅ Protect internal database fields using response models

---

# 🚀 Next Stage

In the next stage, you will learn:

- Relationships (One-to-Many)
- Foreign Keys
- Authentication
- JWT Tokens
- User Login
- Protected Routes
- Dependency Injection
- Advanced CRUD Operations

---

# 📚 References

## Official Documentation

- FastAPI Documentation: https://fastapi.tiangolo.com/
- SQLModel Documentation: https://sqlmodel.tiangolo.com/
- SQLAlchemy Documentation: https://docs.sqlalchemy.org/
- Alembic Documentation: https://alembic.sqlalchemy.org/
- SQLite Documentation: https://sqlite.org/

---

# ⭐ Why SQLModel & Alembic?

SQLModel combines the power of SQLAlchemy with Pydantic, making it easy to build type-safe database models for FastAPI applications. Alembic provides a reliable migration system that tracks database schema changes, allowing developers to evolve the database safely without manually modifying tables.
