# Inventory Management System API

## Project Overview

This project is a **RESTful API** for an **Inventory Management System** built using **Django Rest Framework**. It allows users to perform **CRUD operations** (Create, Read, Update, Delete) on inventory items and is secured with **JWT-based authentication**. The system uses **PostgreSQL** as the database and **Redis** for caching frequently accessed items.

---

## Features

- **CRUD Operations**: Create, Read, Update, and Delete inventory items.
- **JWT Authentication**: Secures the API endpoints to allow access only to authenticated users.
- **PostgreSQL Database**: Stores inventory data persistently.
- **Redis Caching**: Improves performance by caching frequently accessed items.
- **Logging**: Integrated logging for debugging and monitoring API usage.
- **Unit Testing**: Comprehensive tests to ensure the reliability of the application.

---

## Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.x**
- **PostgreSQL**
- **Redis**
- **Django** and **Django Rest Framework**
- **djangorestframework-simplejwt** (for JWT)
- **django-redis** (for Redis integration)

---

## Installation and Setup

### 1. Set Up Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 2. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Configure PostgreSQL Database

Ensure PostgreSQL is installed and running. Create a database and user:

```sql
CREATE DATABASE inventory_db;
CREATE USER postgres_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE inventory_db TO postgres_user;
```

Update the **`DATABASES`** section in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventory_db',
        'USER': 'postgres_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Set Up Redis

Ensure Redis is running:

```bash
sudo service redis-server start
```

Configure caching in `settings.py`:

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### 5. Run Database Migrations

Run the migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Admin)

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### 7. Run the Server

Finally, start the Django development server:

```bash
python manage.py runserver
```

---

## API Documentation

### Authentication

Before accessing any endpoints, users must authenticate by obtaining a **JWT token**.

#### 1. Obtain Access and Refresh Tokens

- **URL**: `/api/token/`
- **Method**: `POST`
- **Request Body**:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

- **Response**:

```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

#### 2. Refresh Access Token

- **URL**: `/api/token/refresh/`
- **Method**: `POST`
- **Request Body**:

```json
{
  "refresh": "<refresh_token>"
}
```

---

### CRUD Operations

#### 1. Create an Item

- **URL**: `/api/items/create/`
- **Method**: `POST`
- **Headers**: 
  - `Authorization`: `Bearer <access_token>`
- **Request Body** (JSON):

```json
{
  "name": "Laptop",
  "description": "A high-performance portable computer"
}
```

- **Response** (Success: 201 Created):

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "A high-performance portable computer",
  "created_at": "2024-10-03T12:00:00Z",
  "updated_at": "2024-10-03T12:00:00Z"
}
```

#### 2. Retrieve All Items

- **URL**: `/api/items/`
- **Method**: `GET`
- **Headers**:
  - `Authorization`: `Bearer <access_token>`
- **Response** (Success: 200 OK):

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "description": "A high-performance portable computer",
    "created_at": "2024-10-03T12:00:00Z",
    "updated_at": "2024-10-03T12:00:00Z"
  },
  {
    "id": 2,
    "name": "Smartphone",
    "description": "A high-end mobile phone",
    "created_at": "2024-10-03T13:00:00Z",
    "updated_at": "2024-10-03T13:00:00Z"
  }
]
```

#### 3. Retrieve a Single Item

- **URL**: `/api/items/<id>/`
- **Method**: `GET`
- **Headers**:
  - `Authorization`: `Bearer <access_token>`
- **Response** (Success: 200 OK):

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "A high-performance portable computer",
  "created_at": "2024-10-03T12:00:00Z",
  "updated_at": "2024-10-03T12:00:00Z"
}
```

#### 4. Update an Item

- **URL**: `/api/items/<id>/`
- **Method**: `PUT`
- **Headers**:
  - `Authorization`: `Bearer <access_token>`
- **Request Body** (JSON):

```json
{
  "name": "Laptop",
  "description": "An updated description for the item"
}
```

- **Response** (Success: 200 OK):

```json
{
  "id": 1,
  "name": "Laptop",
  "description": "An updated description for the item",
  "created_at": "2024-10-03T12:00:00Z",
  "updated_at": "2024-10-03T14:00:00Z"
}
```

#### 5. Delete an Item

- **URL**: `/api/items/<id>/`
- **Method**: `DELETE`
- **Headers**:
  - `Authorization`: `Bearer <access_token>`
- **Response** (Success: 204 No Content)

---

## Testing

Run unit tests to ensure the API is functioning as expected:

```bash
python manage.py test
```

---

## Logging

Logs are stored in `inventory.log` and contain detailed information about API usage, errors, and other significant events.

---
