# FastAPI Stage 6 – Error Handling, Standardized Responses & CORS

## Overview

This project is the sixth stage of learning **FastAPI** by implementing **global exception handling**, **standardized API responses**, **CORS middleware**, and **proper HTTP status codes**.

The objective of this stage is to make every API response predictable and consistent. All errors are handled through a global exception handler, and Cross-Origin Resource Sharing (CORS) is configured to allow frontend applications to communicate with the backend securely.

---

# Learning Objectives

After completing this stage, you will understand:

- How to implement global exception handling
- How to create standardized API responses
- How to handle validation and runtime errors
- How CORS works and why it is required
- How to configure CORS middleware in FastAPI
- How to return proper HTTP status codes
- How to build frontend-friendly REST APIs

---

# Technologies Used

- Python 3.14
- FastAPI
- SQLModel
- SQLite
- Pydantic v2
- Uvicorn

---

# Project Structure

```
FastAPI-Learning/
│
├── alembic/
│
├── core/
│   ├── __init__.py
│   └── exception_handler.py
│
├── repository/
│   ├── __init__.py
│   └── hero_repository.py
│
├── schemas/
│   ├── __init__.py
│   └── response.py
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

# Features Implemented

## Global Exception Handling

Implemented centralized exception handling using FastAPI exception handlers.

Handled exceptions include:

- HTTPException
- RequestValidationError
- Generic Exception

All errors now return a standardized JSON response.

---

## Standardized Error Response

Instead of returning different error formats, every error follows the same structure.

Example:

```json
{
    "error": {
        "code": 404,
        "message": "Hero not found"
    }
}
```

This provides a consistent response format for frontend applications.

---

## Standardized Success Responses

Successful API requests return appropriate HTTP status codes with structured response models.

Example:

```json
{
    "id": 1,
    "name": "Spider-Man",
    "age": 21
}
```

---

## CORS Middleware

Configured Cross-Origin Resource Sharing (CORS) to allow frontend applications to access the API.

Configured origins:

```python
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

Middleware configuration:

- Allow Origins
- Allow Credentials
- Allow Methods
- Allow Headers

---

## Proper HTTP Status Codes

Implemented REST API status codes.

| Operation | Status Code |
|-----------|-------------|
| Create Hero | **201 Created** |
| Read Hero(s) | **200 OK** |
| Update Hero | **200 OK** |
| Delete Hero | **204 No Content** |
| Hero Not Found | **404 Not Found** |
| Validation Error | **422 Unprocessable Entity** |
| Internal Server Error | **500 Internal Server Error** |

---

# Error Handling Flow

```
Client
   │
   ▼
FastAPI Route
   │
   ▼
Service Layer
   │
   ▼
Repository Layer
   │
   ▼
Database

        ▲
        │
Global Exception Handler
        │
        ▼
Standardized Error Response
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| POST | `/heroes/` | Create Hero |
| GET | `/heroes/` | Retrieve All Heroes |
| GET | `/heroes/{hero_id}` | Retrieve Hero by ID |
| PATCH | `/heroes/{hero_id}` | Update Hero |
| DELETE | `/heroes/{hero_id}` | Delete Hero |

---

# Response Examples

## Success Response

```json
{
    "id": 1,
    "name": "Spider-Man",
    "age": 21
}
```

Status:

```
201 Created
```

---

## Hero Not Found

```json
{
    "error": {
        "code": 404,
        "message": "Hero not found"
    }
}
```

---

## Validation Error

```json
{
    "error": {
        "code": 422,
        "message": "Validation Error"
    }
}
```

---

## Internal Server Error

```json
{
    "error": {
        "code": 500,
        "message": "Internal Server Error"
    }
}
```

---

# Running the Application

Start the FastAPI development server:

```bash
fastapi dev main.py
```

Or using Uvicorn:

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

# Testing

## Create Hero

```http
POST /heroes/
```

Expected Status:

```
201 Created
```

---

## Retrieve Heroes

```http
GET /heroes/
```

Expected Status:

```
200 OK
```

---

## Update Hero

```http
PATCH /heroes/{hero_id}
```

Expected Status:

```
200 OK
```

---

## Delete Hero

```http
DELETE /heroes/{hero_id}
```

Expected Status:

```
204 No Content
```

---

## Invalid Hero

```http
GET /heroes/999
```

Expected Response:

```json
{
    "error": {
        "code": 404,
        "message": "Hero not found"
    }
}
```

---

## Invalid Request Body

Expected Status:

```
422 Unprocessable Entity
```

---

# Benefits

- Consistent API responses
- Centralized exception handling
- Better frontend integration
- Proper REST API status codes
- Secure browser communication with CORS
- Improved maintainability
- Cleaner application architecture

---

# GitHub Repository

**Repository:**

https://github.com/Bharathisam/Backend_development

**Stage 6 Branch:**

https://github.com/Bharathisam/Backend_development/tree/stage6

Clone the repository:

```bash
git clone https://github.com/Bharathisam/Backend_development.git
```

Switch to the Stage 6 branch:

```bash
git checkout stage6
```

---

# Learning Outcomes

By completing this stage, you learned how to:

- Implement global exception handling
- Create standardized API response models
- Handle HTTP and validation errors consistently
- Configure CORS middleware for frontend integration
- Return proper HTTP status codes
- Build production-ready REST API responses
- Improve API reliability and maintainability

---

# Stage Status

**Completed**

Implemented:

- Global Exception Handling
- Standardized Error Responses
- Standardized Response Models
- CORS Middleware
- Proper HTTP Status Codes
- Swagger API Testing
- Layered Architecture
- Service & Repository Pattern
- SQLModel Integration
- SQLite Database
```
