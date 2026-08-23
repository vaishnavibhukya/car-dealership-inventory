# Car Dealership Inventory Management System

A full-stack web application for managing and tracking vehicles in a car dealership inventory.

## Features

- User registration and login
- Secure authentication
- Add new vehicles to inventory
- View all available vehicles
- Search vehicles
- Update vehicle information
- Delete vehicles
- Purchase/sell vehicles
- Track vehicle availability
- Track vehicle quantity
- Record vehicle sales
- Dashboard for inventory management
- REST API based backend
- SQLite database for storing application data
- Responsive and user-friendly interface

## Tech Stack

### Frontend

- React.js
- JavaScript
- HTML5
- CSS3
- Vite

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

### Tools

- Git
- GitHub
- VS Code
- REST API

## Project Structure

```text
Car-Dealership-Inventory/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── tests/
│   ├── cars.db
│   ├── pytest.ini
│   └── README.md
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── assets/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── package.json
├── package-lock.json
└── README.md