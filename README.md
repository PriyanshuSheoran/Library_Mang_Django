# Library Management System with Django REST Framework

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

A RESTful API for library management with JWT authentication and role-based access control.

## Project Structure
```
library_manag_django/
├── library/  # Main app
│   ├── migrations/  # Database migrations
│   ├── __init__.py
│   ├── admin.py  # Admin configuration
│   ├── apps.py  # App config
│   ├── models.py  # Data models
│   ├── serializers.py  # DRF serializers
│   ├── tests.py  # Test cases
│   ├── urls.py  # App URLs
│   └── views.py  # View logic
│
├── library_manag_django/  # Project config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py  # Project settings
│   ├── urls.py  # Root URLs
│   └── wsgi.py
│
├── venv/  # Virtual environment
├── .gitignore
├── db.sqlite3  # Development database
├── manage.py
├── README.md  # This file
└── requirements.txt  # Dependencies
```

## Features

- 📚 Book management (CRUD operations)
- 👥 JWT authentication
- 🔒 Role-based access (Admin/User)
- 📅 Book borrowing system
- ✅ Comprehensive testing

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/library-management-drf.git
cd library-management-drf
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
```bash
python manage.py migrate
```

### 5. Create Admin User
```bash
python manage.py createsuperuser
```

### 6. Run Server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
| Endpoint       | Method | Description       |
|---------------|--------|-------------------|
| `/auth/signup` | POST  | Register user    |
| `/auth/login`  | POST  | Get JWT tokens   |
| `/auth/refresh` | POST  | Refresh token    |
| `/auth/logout` | POST  | Invalidate token |
| `/auth/me`     | GET   | User details     |

### Admin Endpoints
| Endpoint            | Method       | Description         |
|---------------------|-------------|---------------------|
| `/admin/books`      | GET         | List books         |
| `/admin/books`      | POST        | Add book           |
| `/admin/books/{id}` | GET/PUT/DELETE | Book operations |
| `/admin/borrowed-books` | GET | List borrows |

## Testing

### Run Tests
```bash
pytest
```

### Test Coverage
```bash
pytest --cov=library --cov-report=html
```

## Deployment

For production:
- Set `DEBUG = False` in `settings.py`
- Configure database (PostgreSQL recommended)
- Set up static files
- Configure allowed hosts

## License

MIT License - see [LICENSE](LICENSE) for details.

