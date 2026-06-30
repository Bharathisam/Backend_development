# FastAPI Stage 5 – Business Logic and Data Access

## Overview

This project is the fifth stage of learning **FastAPI** by implementing a clean project architecture using the **Service Layer** and **Repository Pattern**.

The objective of this stage is to separate API routes, business logic, and database access into independent layers. This improves code readability, maintainability, scalability, and makes the application easier to test.

---

# Learning Objectives

After completing this stage, you will understand:

- How to separate business logic from API routes
- How to implement the Service Layer pattern
- How to implement the Repository Pattern
- How to organize FastAPI projects using a layered architecture
- How to keep route functions clean and readable
- How to improve code maintainability and scalability

---

# Technologies Used

- Python 3.14
- FastAPI
- SQLModel
- SQLite
- Uvicorn
- Pydantic v2

---

# Project Structure

```
FastAPI-Learning/
│
├── alembic/
│
├── repository/
│   ├── __init__.py
│   └── hero_repository.py
│
├── services/
│   ├── __init__.py
│   └── hero_service.py
│
├── database.db
├── database.py
├── main.py
├── models.py
├── pyproject.toml
└── README.md
```

---

# Architecture

```
Client
   │
   ▼
FastAPI Routes (main.py)
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
SQLite Database
```

---

# Features Implemented

## Thin Route Functions

The API routes are responsible only for:

- Receiving requests
- Calling the appropriate service
- Returning the response

Example:

```python
@app.post("/heroes/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    return hero_service.create_hero(session, hero)
```

---

## Service Layer

The Service Layer contains the application's business logic.

Responsibilities include:

- Validating application workflow
- Handling business rules
- Managing exceptions
- Calling the Repository Layer

Implemented functions:

- Create Hero
- Read All Heroes
- Read Hero by ID
- Update Hero
- Delete Hero

---

## Repository Layer

The Repository Layer is responsible for database operations.

Responsibilities include:

- Insert records
- Retrieve records
- Update records
- Delete records

Implemented functions:

- create_hero()
- get_all_heroes()
- get_hero_by_id()
- update_hero()
- delete_hero()

---

## CRUD Operations

| Method | Endpoint | Description |
|---------|-----------|-------------|
| POST | `/heroes/` | Create Hero |
| GET | `/heroes/` | Retrieve All Heroes |
| GET | `/heroes/{hero_id}` | Retrieve Hero by ID |
| PATCH | `/heroes/{hero_id}` | Update Hero |
| DELETE | `/heroes/{hero_id}` | Delete Hero |

---

# Separation of Responsibilities

| Layer | Responsibility |
|--------|----------------|
| main.py | API Routes |
| hero_service.py | Business Logic |
| hero_repository.py | Database Operations |
| models.py | SQLModel Models |
| database.py | Database Configuration |

---

# Benefits of the Architecture

- Better code organization
- Easier maintenance
- Improved readability
- Reusable business logic
- Easier testing
- Scalable project structure
- Separation of concerns

---

# Running the Application

Start the development server:

```bash
fastapi dev main.py
```

Or using Uvicorn:

```bash
uvicorn main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# API Testing

## Create Hero

```json
{
  "name": "Iron Man",
  "age": 45,
  "secret_name": "Tony Stark"
}
```

Result:

```
200 OK
```

---

## Retrieve Heroes

```
GET /heroes/
```

---

## Retrieve Hero by ID

```
GET /heroes/1
```

---

## Update Hero

```json
{
  "age": 46
}
```

---

## Delete Hero

```
DELETE /heroes/1
```

Returns:

```json
{
  "ok": true
}
```

---

# Design Patterns Used

## Service Layer Pattern

The Service Layer contains all business logic and acts as an intermediary between the API routes and the Repository Layer.

## Repository Pattern

The Repository Layer abstracts database operations from the rest of the application, allowing cleaner and more maintainable code.

## Separation of Concerns (SoC)

Each layer has a single responsibility:

- Routes handle HTTP requests.
- Services handle business logic.
- Repositories handle database access.

---

# GitHub Repository

**Repository:**

https://github.com/Bharathisam/Backend_development

**Stage 5 Branch:**

https://github.com/Bharathisam/Backend_development/tree/stage5

Clone the repository:

```bash
git clone https://github.com/Bharathisam/Backend_development.git
```

Switch to the Stage 5 branch:

```bash
git checkout stage5
```

---

# Learning Outcomes

By completing this stage, you learned how to:

- Build a layered FastAPI application
- Separate API routes from business logic
- Implement the Service Layer pattern
- Implement the Repository Pattern
- Organize code using Separation of Concerns
- Create a maintainable and scalable backend architecture

---

# Stage Status

**Completed**

Implemented:

- Service Layer
- Repository Pattern
- Layered Architecture
- Thin Route Functions
- CRUD Operations
- SQLModel Integration
- SQLite Database
- Swagger API Testing
- Clean Project Structure
