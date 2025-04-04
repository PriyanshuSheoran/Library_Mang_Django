# Library Management System with Django REST Framework

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A RESTful API for library management with JWT authentication and role-based access control.

## Project Structure
library_manag_django/ # Project root
├── library/ # Main Django app
│ ├── migrations/ # Database migrations
│ ├── init.py
│ ├── admin.py # Admin site configuration
│ ├── apps.py # App configuration
│ ├── models.py # Data models (User, Book, BorrowedBook)
│ ├── serializers.py # DRF serializers
│ ├── urls.py # App URL routes
│ ├── views.py # View functions/classes
│ └── tests.py # Test cases
│
├── library_manag_django/ # Project configuration
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py # Project settings
│ ├── urls.py # Main URL router
│ └── wsgi.py
│
├── venv/ # Virtual environment (ignored in git)
├── .gitignore # Git ignore rules
├── db.sqlite3 # Development database (ignored in git)
├── manage.py # Django management script
├── README.md # This file
└── requirements.txt # Project dependencies

## Features

- 📚 Book management (CRUD operations)
- 👥 User authentication with JWT
- 🔒 Role-based access control (Admin/User)
- 📅 Book borrowing/returning system
- 📊 Admin dashboard for management
- ✅ Comprehensive API documentation

## Prerequisites

- Python 3.8+
- Django 4.2+
- Django REST Framework
- PostgreSQL (recommended) or SQLite

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/library-management-drf.git
   cd library-management-drf
Set up virtual environment

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
pip install -r requirements.txt
Database setup

bash
Copy
python manage.py migrate
Create superuser

bash
Copy
python manage.py createsuperuser
Run development server

bash
Copy
python manage.py runserver
API Endpoints
Authentication
Endpoint	Method	Description
/auth/signup	POST	User registration
/auth/login	POST	Get JWT tokens
/auth/refresh	POST	Refresh access token
/auth/logout	POST	Invalidate refresh token
/auth/me	GET	Get current user details
/auth/me	PUT	Update user details
Admin Endpoints (Require admin privileges)
Endpoint	Method	Description
/admin/books	GET	List all books
/admin/books	POST	Add new book
/admin/books/{id}	GET	Get book details
/admin/books/{id}	PUT	Update book
/admin/books/{id}	DELETE	Delete book
/admin/borrowed-books	GET	List all borrowed books
Models
User
Custom user model extending AbstractUser

Role-based authentication (admin/user)

Book
Title, author, ISBN (unique)

Published date, stock count

BorrowedBook
User-book relationship

Borrow/return dates

Return status

Testing
Run tests with pytest:

bash
Copy
pytest
Configuration
Update settings.py for production:

Set DEBUG = False

Configure database (PostgreSQL recommended)

Add allowed hosts

Set up static files

Configure JWT settings


Contributing
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

License
Distributed under the MIT License. See LICENSE for more information.

