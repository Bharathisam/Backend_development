# 🚀 FastAPI Stage 2 – Request & Response Models with Pydantic

## 📖 Overview

This project is the second stage of learning **FastAPI** by implementing **request validation** and **response models** using **Pydantic**.

The objective of this stage is to understand how FastAPI validates incoming request data, serializes responses, and automatically generates API documentation.

---

# 🎯 Learning Objectives

After completing this stage, you will understand:

- What Pydantic models are
- Request body validation
- Response models
- Data serialization
- Email validation
- FastAPI automatic documentation
- OpenAPI schema generation

---

# 📂 Project Structure

```text
FastAPI-Stage2/
│
├── main.py              # FastAPI application
├── pyproject.toml       # FastAPI configuration
├── README.md
└── .gitignore
```

---

# ⚙️ Prerequisites

Before starting, make sure you have installed:

- Python 3.11 or later
- pip
- Virtual Environment (venv)

Check your Python version:

```bash
python --version
```

---

# 🛠️ Installation

## 1. Clone the Repository

```bash
git clone <repository-url>
cd FastAPI-Stage2
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
pip install "fastapi[standard]" email-validator
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

# 📌 API Endpoints

## GET /

Returns a simple greeting message.

### Response

```json
{
  "message": "Hello World"
}
```

---

## POST /items/

Creates a new item and automatically calculates the total price including tax.

### Request

```json
{
  "name": "Laptop",
  "description": "Gaming Laptop",
  "price": 50000,
  "tax": 5000
}
```

### Response

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "Gaming Laptop",
  "price": 50000,
  "tax": 5000,
  "price_with_tax": 55000
}
```

---

## GET /items/{item_id}

Returns an item using the provided item ID.

### Example

```http
GET /items/1
```

### Response

```json
{
  "id": 1,
  "name": "Sample Item",
  "description": "A sample item description",
  "price": 99.99,
  "tax": 8.99,
  "price_with_tax": 108.98
}
```

---

## POST /user/

Creates a new user.

### Request

```json
{
  "username": "bharathi",
  "email": "bharathi@example.com",
  "full_name": "Bharathi S",
  "password": "secret123"
}
```

### Response

```json
{
  "username": "bharathi",
  "email": "bharathi@example.com",
  "full_name": "Bharathi S"
}
```

> **Note:** The password is not returned because the API uses `response_model=UserOut`.

---

# 🧪 Testing the API

## Using Swagger UI

Open:

```
http://127.0.0.1:8000/docs
```

1. Select an endpoint.
2. Click **Try it out**.
3. Enter the request body (if required).
4. Click **Execute**.
5. View the response.

---

# 📚 Understanding the Code

## Pydantic Models

The project uses the following models:

### Item Models

- `ItemBase`
- `ItemCreate`
- `ItemResponse`

### User Models

- `UserBase`
- `UserIn`
- `UserOut`

These models provide:

- Automatic validation
- Type checking
- JSON serialization
- API documentation generation

---

## Request Validation

FastAPI validates incoming JSON automatically before executing the endpoint.

Example:

```python
class UserIn(UserBase):
    password: str
```

---

## Response Model

```python
@app.post("/user/", response_model=UserOut)
```

FastAPI automatically removes fields that are not included in `UserOut`.

---

## Email Validation

```python
email: EmailStr
```

FastAPI validates email addresses automatically using Pydantic.

---

# 📖 Automatic API Documentation

FastAPI automatically generates API documentation using the **OpenAPI** specification.

## Swagger UI

```
/docs
```

Features:

- Interactive API testing
- Request validation
- Response schemas
- API documentation

---

## ReDoc

```
/redoc
```

Provides a clean and readable API reference.

---

## OpenAPI Schema

```
/openapi.json
```

Contains the complete OpenAPI specification in JSON format.

---

# 💡 Key Concepts Learned

- Pydantic Models
- Request Body Validation
- Response Models
- Email Validation
- JSON Serialization
- Automatic API Documentation
- OpenAPI Specification
- FastAPI CLI
- Async API Development

---

# 🛠️ Technologies Used

| Technology | Version |
|------------|----------|
| Python | 3.11+ |
| FastAPI | Latest |
| Pydantic | v2 |
| Uvicorn | Latest |
| OpenAPI | 3.1 |

---

# 📈 Learning Outcomes

By completing this stage, you can:

- ✅ Create Pydantic models
- ✅ Validate request bodies
- ✅ Use response models
- ✅ Validate email addresses
- ✅ Build REST APIs with FastAPI
- ✅ Test APIs using Swagger UI
- ✅ Understand automatic API documentation

---

# 🚀 Next Stage

In the next stage, you will learn:

- Path Parameters
- Query Parameters
- HTTP Status Codes
- Dependency Injection
- Exception Handling
- CRUD Operations
- Database Integration
- SQLAlchemy
- Authentication & Authorization

---

# 📚 References

## Official Documentation

- FastAPI Documentation: https://fastapi.tiangolo.com/
- FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/
- Pydantic Documentation: https://docs.pydantic.dev/
- Uvicorn Documentation: https://www.uvicorn.org/

---

# ⭐ Why Pydantic?

Pydantic provides powerful data validation using Python type hints. FastAPI integrates with Pydantic to automatically validate incoming requests, serialize responses, and generate interactive API documentation, making backend development faster, safer, and more maintainable.
