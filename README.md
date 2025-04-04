# Library Management System with Django REST Framework

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A RESTful API for library management with JWT authentication and role-based access control.

## Project Structure
library_manag_django/
├── library/ # Main app
│ ├── migrations/ # Database migrations
│ ├── init.py
│ ├── admin.py # Admin configuration
│ ├── apps.py # App config
│ ├── models.py # Data models
│ ├── serializers.py # DRF serializers
│ ├── tests.py # Test cases
│ ├── urls.py # App URLs
│ └── views.py # View logic
│
├── library_manag_django/ # Project config
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py # Project settings
│ ├── urls.py # Root URLs
│ └── wsgi.py
│
├── venv/ # Virtual env
├── .gitignore
├── db.sqlite3 # Dev database
├── manage.py
├── README.md # This file
└── requirements.txt # Dependencies

Copy

## Features

- 📚 Book management (CRUD operations)
- 👥 JWT authentication
- 🔒 Role-based access (Admin/User)
- 📅 Book borrowing system
- ✅ Comprehensive testing

## Installation

1. Clone repository:
```bash
git clone https://github.com/yourusername/library-management-drf.git
cd library-management-drf
Set up virtual environment:

bash
Copy
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
pip install -r requirements.txt
Configure database:

bash
Copy
python manage.py migrate
Create admin user:

bash
Copy
python manage.py createsuperuser
Run server:

bash
Copy
python manage.py runserver
API Endpoints
Authentication
Endpoint	Method	Description
/auth/signup	POST	Register user
/auth/login	POST	Get JWT tokens
/auth/refresh	POST	Refresh token
/auth/logout	POST	Invalidate token
/auth/me	GET	User details
Admin Endpoints
Endpoint	Method	Description
/admin/books	GET	List books
/admin/books	POST	Add book
/admin/books/{id}	GET/PUT/DELETE	Book operations
/admin/borrowed-books	GET	List borrows
Testing
Run tests with:

bash
Copy
pytest
Test coverage:

bash
Copy
pytest --cov=library --cov-report=html
Deployment
For production:

Set DEBUG = False in settings.py

Configure database (PostgreSQL recommended)

Set up static files

Configure allowed hosts

License
MIT License - see LICENSE for details.

Copy
