# API Handoff Document

## Overview

This project provides a RESTful Hero Management API built using FastAPI.

The API supports complete CRUD operations and follows standardized request and response formats.

---

## Base URLs

### Development

```
http://127.0.0.1:8000
```

### Staging

```
Not deployed
```

---

## API Documentation

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Authentication

This project currently does not require authentication.

Future versions may implement JWT Authentication.

---

## Available Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /heroes/ | Create Hero |
| GET | /heroes/ | Get All Heroes |
| GET | /heroes/{hero_id} | Get Hero By ID |
| PATCH | /heroes/{hero_id} | Update Hero |
| DELETE | /heroes/{hero_id} | Delete Hero |

---

## Sample Request

```json
{
    "name": "Batman",
    "age": 35,
    "secret_name": "Bruce Wayne"
}
```

---

## Successful Response

```json
{
    "id": 1,
    "name": "Batman",
    "age": 35
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

## Not Found Error

```json
{
    "error": {
        "code": 404,
        "message": "Hero not found"
    }
}
```

---

## Sample Data

Example requests are available in:

```
docs/sample_data.json
```

---

## Postman Collection

The exported Postman collection is available in:

```
docs/Hero_API.postman_collection.json
```

---

## Notes for Frontend Developers

- Use the Development Base URL during local development.
- API responses are returned in JSON format.
- Validation errors return HTTP 422.
- Missing resources return HTTP 404.
- Successful delete operations return HTTP 204 No Content.
- Swagger UI can be used to explore and test all endpoints.