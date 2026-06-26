# 🚀 FastAPI Stage 1 – Hello World API

## 📖 Overview

This project is the first stage of learning **FastAPI** by implementing a simple **Hello World API** using the official FastAPI tutorial.

The purpose of this stage is to understand the basic structure of a FastAPI application, how to create API endpoints, and how FastAPI automatically generates interactive API documentation.

---

## 🎯 Learning Objectives

After completing this stage, you will understand:

- What FastAPI is
- How to create a FastAPI application
- How to define API endpoints
- How to run a FastAPI server
- How to use automatic Swagger UI documentation
- How OpenAPI documentation is generated automatically

---

# 📂 Project Structure

```
FastAPI-HelloWorld/
│
├── main.py              # FastAPI application
├── pyproject.toml       # FastAPI configuration
└── README.md
```

---

# 📝 Source Code

### main.py

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

---

### pyproject.toml

```toml
[tool.fastapi]
entrypoint = "main:app"
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
cd FastAPI-HelloWorld
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

## 4. Install FastAPI

```bash
pip install "fastapi[standard]"
```

---

## 5. Run Development Server

```bash
fastapi dev
```

---

# 🌐 Application URLs

Once the server starts, open the following URLs:

| Service | URL |
|----------|-----|
| Main Application | http://127.0.0.1:8000 |
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |
| OpenAPI JSON | http://127.0.0.1:8000/openapi.json |

---

# 📌 API Endpoint

## GET /

Returns a simple greeting message.

### Request

```http
GET /
```

### Response

```json
{
    "message": "Hello World"
}
```

---

# 🧪 Testing the API

### Using Browser

Open

```
http://127.0.0.1:8000/
```

Response

```json
{
    "message": "Hello World"
}
```

---

### Using Swagger UI

1. Open

```
http://127.0.0.1:8000/docs
```

2. Click **GET /**

3. Click **Try it out**

4. Click **Execute**

5. View the response.

---

# 📚 Understanding the Code

### FastAPI Instance

```python
app = FastAPI()
```

Creates the FastAPI application.

---

### Path Operation Decorator

```python
@app.get("/")
```

Defines an HTTP **GET** endpoint.

---

### Path Operation Function

```python
async def root():
```

Handles incoming requests for the root endpoint.

---

### JSON Response

```python
return {"message": "Hello World"}
```

FastAPI automatically converts Python dictionaries into JSON responses.

---

# 📖 Automatic API Documentation

FastAPI automatically generates API documentation using the **OpenAPI** specification.

## Swagger UI

```
/docs
```

Features:

- Interactive API testing
- Request and response schemas
- API endpoint documentation
- Execute APIs directly from the browser

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

- FastAPI application structure
- Creating REST APIs
- HTTP GET method
- Path operations
- Async functions
- JSON responses
- Automatic API documentation
- OpenAPI specification
- FastAPI CLI
- Development server

---

# 🛠️ Technologies Used

| Technology | Version |
|------------|----------|
| Python | 3.11+ |
| FastAPI | 0.138.0 |
| Uvicorn | 0.49.0 |
| OpenAPI | 3.1 |

---

# 📈 Learning Outcomes

By completing this stage, you can:

- ✅ Build your first FastAPI application
- ✅ Create REST API endpoints
- ✅ Run a local development server
- ✅ Test APIs using Swagger UI
- ✅ Understand FastAPI project structure
- ✅ Explore automatically generated API documentation

---

# 🚀 Next Stage

In the next stage, you will learn:

- Path Parameters
- Query Parameters
- Request Body Validation
- Pydantic Models
- Response Models
- HTTP Status Codes
- Error Handling
- CRUD APIs
- Database Integration
- Authentication & Authorization

---

# 📚 References

## Official Documentation

- FastAPI Documentation: https://fastapi.tiangolo.com/
- FastAPI Tutorial: https://fastapi.tiangolo.com/tutorial/
- Uvicorn Documentation: https://www.uvicorn.org/
- OpenAPI Specification: https://www.openapis.org/

---

# ⭐ Why FastAPI?

FastAPI is a modern, high-performance Python web framework for building APIs with automatic validation, interactive documentation, asynchronous support, and excellent developer productivity. It is widely used for backend development, microservices, and machine learning APIs.

