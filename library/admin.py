
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Book, BorrowedBook

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)
    search_fields = ('username', 'email')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'stock')
    search_fields = ('title', 'author', 'isbn')

@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_date', 'returned')
    list_filter = ('returned',)
    search_fields = ('user__username', 'book__title')