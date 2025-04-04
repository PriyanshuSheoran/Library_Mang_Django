
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
    UserProfileView,
    BookListView,
    BookDetailView,
    BorrowedBookListView
)

urlpatterns = [
    
    path('signup', UserRegisterView.as_view(), name='signup'),
    path('login', UserLoginView.as_view(), name='login'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('me', UserProfileView.as_view(), name='user_profile'),
    
    
    path('admin/books', BookListView.as_view(), name='book_list'),
    path('admin/books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('admin/borrowed-books', BorrowedBookListView.as_view(), name='borrowed_books'),
]