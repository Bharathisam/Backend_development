#  Stage 7 – Testing & Contract Testing

## Overview

This project is the seventh stage of learning **FastAPI** by implementing **automated API testing** and **contract testing**.

The objective of this stage is to ensure that the API behaves correctly through automated tests and that it continues to match its published OpenAPI specification. This helps detect regressions early and guarantees reliable communication between the backend and frontend.

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
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_heroes.py
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

## Automated Testing

Implemented automated API testing using **Pytest** and **FastAPI TestClient**.

Benefits include:

- Automated endpoint verification
- Faster regression testing
- Repeatable test execution
- Reliable API behavior

---

## TestClient

Used FastAPI's TestClient to simulate HTTP requests without running the server manually.

Supported operations include:

- POST
- GET
- PATCH
- DELETE

---

## Happy Path Testing

Implemented a successful API test to verify that a Hero can be created correctly.

Verified:

- HTTP Status Code **201 Created**
- Response data
- Generated Hero ID

---

## Validation Error Testing

Implemented a validation test by sending invalid request data.

Verified:

- HTTP Status Code **422 Unprocessable Entity**
- Standardized error response
- Request validation behavior

---

## Contract Testing

Implemented contract testing using **Schemathesis**.

Schemathesis automatically:

- Reads the OpenAPI specification
- Generates test cases
- Validates request and response contracts
- Detects undocumented responses
- Finds API edge cases automatically

---

# Test Coverage

The following automated tests were implemented:

| Test | Description |
|------|-------------|
| Create Hero | Happy path test |
| Validation Error | Invalid request data |

---

# Running the Tests

Run all automated tests:

```bash
pytest
```

Expected output:

```text
=========================
collected 2 items

tests/test_heroes.py ..

=========================
2 passed
=========================
```

---

# Contract Testing

Start the FastAPI application:

```bash
fastapi dev main.py
```

Run Schemathesis:

```bash
schemathesis run http://127.0.0.1:8000/openapi.json
```

Schemathesis automatically validates the API against the published OpenAPI specification.

---

# API Endpoints Tested

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/heroes/` | Create Hero |
| GET | `/heroes/` | Retrieve Heroes |
| GET | `/heroes/{hero_id}` | Retrieve Hero by ID |
| PATCH | `/heroes/{hero_id}` | Update Hero |
| DELETE | `/heroes/{hero_id}` | Delete Hero |

---

# Example Test

## Create Hero

Request:

```json
{
    "name": "Batman",
    "age": 35,
    "secret_name": "Bruce Wayne"
}
```

Expected:

```text
201 Created
```

---

## Validation Error

Request:

```json
{
    "name": "",
    "age": -5,
    "secret_name": ""
}
```

Expected:

```text
422 Unprocessable Entity
```

---

# Testing Workflow

```
Developer
      │
      ▼
Pytest
      │
      ▼
FastAPI TestClient
      │
      ▼
FastAPI Application
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

# Contract Testing Workflow

```
Schemathesis
      │
      ▼
OpenAPI Specification
      │
      ▼
Generate Test Cases
      │
      ▼
Execute API Requests
      │
      ▼
Validate Responses
```

---



# GitHub Repository

**Repository**

https://github.com/Bharathisam/Backend_development

**Stage 7 Branch**

https://github.com/Bharathisam/Backend_development/tree/stage7

Clone the repository:

```bash
git clone https://github.com/Bharathisam/Backend_development.git
```

Switch to the Stage 7 branch:

```bash
git checkout stage7
```
```
