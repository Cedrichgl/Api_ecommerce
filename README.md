# 🛒 E-commerce API

A simple backend API for an e-commerce application.

Built with FastAPI, JWT authentication, and PostgreSQL.

---

## 🚀 Overview

This project provides a backend to:

* manage users and authentication
* handle products and orders
* expose a clean REST API

Designed to be modular and easy to extend.

---

## 🔄 Workflow

```text id="9xq2lm"
Client (Frontend / API call)
        │
        ▼
[API Layer]
(FastAPI endpoints)
        │
        ▼
[Auth Layer]
(JWT - user authentication & security)
        │
        ▼
[Data Validation]
(Pydantic schemas)
        │
        ▼
[Business Logic]
(products, orders, cart)
        │
        ▼
[ORM Layer]
(SQLAlchemy)
        │
        ▼
[Database]
(PostgreSQL)
        │
        ▼
[Migrations]
(Alembic)
```

---

## 🧱 Architecture

* **API Layer (FastAPI)**
  Handles routes and HTTP requests

* **Auth Layer (JWT)**
  Secures endpoints and manages users

* **Validation Layer (Pydantic)**
  Ensures clean and safe input data

* **Service Layer**
  Handles products, orders, and business logic

* **Database Layer (SQLAlchemy)**
  Maps objects to database tables

* **Migrations (Alembic)**
  Manages schema evolution

---

## 🧪 Example Flow

```text id="3k8sja"
Create Order
→ Request sent to API
→ User authenticated (JWT)
→ Data validated (Pydantic)
→ Order processed (business logic)
→ Stored in database (SQLAlchemy)
→ Response returned
```

---

## 📦 Tech Stack

* FastAPI
* JWT (authentication)
* Pydantic
* SQLAlchemy
* Alembic
* PostgreSQL

---

## 🎯 Use Cases

* E-commerce backend
* API for web/mobile shop
* MVP or scalable backend

---

## ⚙️ Installation

```bash id="2d7lq1"
git clone https://github.com/Cedrichgl/Api_ecommerce.git
cd Api_ecommerce
pip install -r requirements.txt
```

