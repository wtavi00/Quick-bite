# 🍔 Quickbite - Student-Friendly Food Delivery Backend

**Quickbite** is a fast, student-oriented food delivery service focused on affordability, health, and convenience. This is the backend system built using **FastAPI**, providing APIs for user management, menu browsing, and order placement.

> 🚀 Designed for university students. Built for speed and simplicity.


## Core Features for Web Backend
### User Management
- Sign up / Login (Students, Admin, Delivery Staff)
- User roles: Customer, Admin, Delivery

### Food Menu Management
- CRUD for snacks, meals, combo deals
- Categorized by price range, food type, and tags.

### Order System
- Place, track, and cancel orders
- Real-time status updates.

### Discounts & Deals
- Student discounts
- Daily combo deals

### Delivery Tracking
- Assign delivery personnel
- Status updates

### Admin Dashboard
- View orders, revenue, top items
- Manage users and meals
- Performance reports


###APIs for Frontend or Mobile App
- RESTful or GraphQL endpoints


---

## 📌 Features

- ⚡ Fast delivery-focused API (15–20 min delivery model)
- 👤 User registration (basic auth ready)
- 📋 Menu creation and browsing
- 🛒 Order placement and tracking
- 🧱 Modular architecture (models, routes, schemas, services)
- 📦 Docker-ready
- 🛠️ Alembic setup for migrations (placeholder)

---

## 🧱 Tech Stack

- **Python 3.10**
- **FastAPI** – Web framework
- **SQLAlchemy** – ORM for database models
- **Pydantic** – Data validation
- **Uvicorn** – ASGI server
- **Alembic** – (for migrations)
- **SQLite** (dev) / **PostgreSQL** (prod-ready)
- **Docker** – Containerization support

---

## 🚀 Getting Started

### 📁 Clone the repo

```bash
git clone https://github.com/wtavi00/Quick-bite.git
cd quickbite-backend
```

##📦 Install dependencies
```bash
pip install -r requirements.txt
```

## ⚙️ Set up environment variables
### Create a .env file:
```bash
DATABASE_URL=sqlite:///./test.db
```
### Or connect to PostgreSQL:
```bash
DATABASE_URL=postgresql://username:password@localhost/quickbite
```

## 🧪 Run the app
```bash
uvicorn app.main:app --reload
```
API docs at: http://localhost:8000/docs

## 🐳 Run with Docker
```bash
docker build -t quickbite-api .
docker run -d -p 8000:8000 quickbite-api
```

## 🧪 API Overview

| Endpoint          | Method | Description          |
| ----------------- | ------ | -------------------- |
| `/users/register` | POST   | Register new user    |
| `/menu/`          | GET    | List all menu items  |
| `/menu/`          | POST   | Create new menu item |
| `/orders/`        | GET    | List all orders      |
| `/orders/`        | POST   | Create a new order   |

## 📂 Project Structure
```bash
quickbite-backend/
│
├── app/
│   ├── main.py           # Entry point
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── routes/           # API routes
│   ├── services/         # Business logic (WIP)
│   ├── db/               # Database connection
│   └── auth/             # Auth logic (WIP)
│
├── tests/                # Test cases
├── alembic/              # Migrations (placeholder)
├── .env                  # Env vars
├── Dockerfile            # Docker setup
├── requirements.txt      # Dependencies
└── README.md             # You are here
```

## 🎯 Future Roadmap
- ✅ User registration
- ⏳ JWT authentication
- ⏳ Admin panel (add/edit menu)
- ⏳ Order status updates
- ⏳ SMS/email notifications
- ⏳ Payment gateway integration
- ⏳ Review system

## Auther
[Avijit Tarafder](https://github.com/wtavi00)

## 📄 License
[MIT License](https://github.com/wtavi00/Quick-bite/blob/main/LICENSE)


