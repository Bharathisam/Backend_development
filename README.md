# FastAPI Stage 4 – Route Registration & Input Validation

## Overview

This project is the fourth stage of learning **FastAPI** by implementing **route registration** and **input validation** using FastAPI and SQLModel.

The objective of this stage is to validate incoming requests before they reach the application logic or database. FastAPI automatically validates request bodies, query parameters, and path parameters, returning clear **422 Unprocessable Entity** responses for invalid input.

---

# Learning Objectives

After completing this stage, you will understand:

- How to register API routes using FastAPI
- How to validate request bodies using SQLModel/Pydantic
- How to validate query parameters
- How to validate path parameters
- How FastAPI automatically returns validation errors (422)
- How Swagger UI documents validation rules automatically

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
├── database.db
├── database.py
├── main.py
├── models.py
├── pyproject.toml
├── README.md
└── venv/
```

---

# Features Implemented

## Route Registration

Registered CRUD API endpoints for Heroes.

| Method | Endpoint | Description |
|---------|-----------|-------------|
| POST | `/heroes/` | Create a new hero |
| GET | `/heroes/` | Retrieve all heroes |
| GET | `/heroes/{hero_id}` | Retrieve hero by ID |
| PATCH | `/heroes/{hero_id}` | Update hero details |
| DELETE | `/heroes/{hero_id}` | Delete hero |

---

## Request Body Validation

Added validation for incoming request data.

Validation rules include:

- Hero name must contain **3–50 characters**
- Secret name must contain **3–100 characters**
- Age must be between **1 and 120**

Example:

```json
{
  "name": "Batman",
  "age": 35,
  "secret_name": "Bruce Wayne"
}
```

---

## Query Parameter Validation

Validated pagination parameters.

| Parameter | Validation |
|-----------|------------|
| offset | Must be ≥ 0 |
| limit | Must be between 1 and 100 |

Example:

```
GET /heroes/?offset=0&limit=10
```

Invalid example:

```
GET /heroes/?limit=500
```

Returns:

```
422 Unprocessable Entity
```

---

## Path Parameter Validation

Validated Hero ID.

Example:

```
GET /heroes/1
```

Invalid example:

```
GET /heroes/-1
```

Returns:

```
422 Unprocessable Entity
```

---

## Automatic Validation Errors

FastAPI automatically rejects malformed requests before reaching the database.

Example invalid request:

```json
{
  "name": "A",
  "age": -5,
  "secret_name": "B"
}
```

Response:

```json
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "String should have at least 3 characters"
    },
    {
      "loc": ["body", "age"],
      "msg": "Input should be greater than or equal to 1"
    }
  ]
}
```

Status Code:

```
422 Unprocessable Entity
```

---

# Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Server URL:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

# Validation Testing

## Valid Request

```json
{
  "name": "Batman",
  "age": 35,
  "secret_name": "Bruce Wayne"
}
```

Result:

```
200 OK
```

---

## Invalid Request Body

```json
{
  "name": "A",
  "age": -5,
  "secret_name": "B"
}
```

Result:

```
422 Unprocessable Entity
```

---

## Invalid Query Parameter

```
GET /heroes/?limit=500
```

Result:

```
422 Unprocessable Entity
```

---

## Invalid Path Parameter

```
GET /heroes/-1
```

Result:

```
422 Unprocessable Entity
```

---

# Learning Outcomes

By completing this stage, you learned how to:

- Register API routes in FastAPI
- Validate request bodies automatically
- Validate query parameters
- Validate path parameters
- Return standardized 422 validation errors
- Improve API reliability by rejecting invalid requests before business logic execution
- Use Swagger UI to test and verify API validation

---

# Stage Status

**Completed**

Implemented:

- Route Registration
- Request Body Validation
- Query Parameter Validation
- Path Parameter Validation
- Automatic 422 Validation Errors
- Swagger API Testing
- SQLModel Integration
```
