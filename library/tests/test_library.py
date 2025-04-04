
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from library.models import Book, BorrowedBook

User = get_user_model()

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def admin_user():
    return User.objects.create_user(
        username='admin',
        password='adminpass',
        is_admin=True
    )

@pytest.fixture
def regular_user():
    return User.objects.create_user(
        username='user',
        password='userpass'
    )

@pytest.fixture
def book():
    return Book.objects.create(
        title='Test Book',
        author='Test Author',
        isbn='1234567890123',
        published_date='2023-01-01',
        stock=5
    )

@pytest.mark.django_db
class TestModels:
    def test_user_creation(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        assert user.username == 'testuser'
        assert not user.is_admin

    def test_book_creation(self, book):
        assert str(book) == 'Test Book'
        assert book.available_copies() == 5

    def test_borrowed_book_creation(self, regular_user, book):
        borrowed = BorrowedBook.objects.create(
            user=regular_user,
            book=book
        )
        assert str(borrowed) == f'{regular_user.username} - {book.title}'
        assert not borrowed.returned

@pytest.mark.django_db
class TestAuthentication:
    def test_user_registration(self, client):
        url = reverse('signup')
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'testpass123'
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username='newuser').exists()

    def test_user_login(self, client, regular_user):
        url = reverse('login')
        data = {
            'username': 'user',
            'password': 'userpass'
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def test_protected_endpoint(self, client, regular_user):
        url = reverse('user_profile')
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
        client.force_authenticate(user=regular_user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
class TestBookViews:
    def test_admin_book_list(self, client, admin_user, book):
        url = reverse('book_list')
        client.force_authenticate(user=admin_user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1
        assert response.data[0]['title'] == 'Test Book'

    def test_book_create_permission(self, client, regular_user):
        url = reverse('book_list')
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'isbn': '9876543210987',
            'published_date': '2023-02-01',
            'stock': 10
        }
        client.force_authenticate(user=regular_user)
        response = client.post(url, data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_book_update(self, client, admin_user, book):
        url = reverse('book_detail', kwargs={'pk': book.pk})
        data = {'title': 'Updated Title'}
        client.force_authenticate(user=admin_user)
        response = client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        book.refresh_from_db()
        assert book.title == 'Updated Title'

@pytest.mark.django_db
class TestBorrowedBookViews:
    def test_borrow_book(self, client, admin_user, regular_user, book):
        url = reverse('borrow_book')
        data = {'book_id': book.pk}
        
        # Regular user can borrow
        client.force_authenticate(user=regular_user)
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert BorrowedBook.objects.count() == 1
        
        # Check available copies decreased
        book.refresh_from_db()
        assert book.available_copies() == 4

    def test_return_book(self, client, admin_user, regular_user, book):
        # First borrow the book
        borrowed = BorrowedBook.objects.create(
            user=regular_user,
            book=book
        )
        
        url = reverse('return_book', kwargs={'pk': borrowed.pk})
        client.force_authenticate(user=regular_user)
        response = client.post(url)
        assert response.status_code == status.HTTP_200_OK
        
        borrowed.refresh_from_db()
        assert borrowed.returned
        assert book.available_copies() == 5