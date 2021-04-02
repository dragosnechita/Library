from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import ListLoaned, ListBooks, AddStudent, AddBook, EditBook, DeleteBook, AddLibrarian, SignUp, AddCategory, ViewBook, SearchByAuthor, SearchByTitle

urlpatterns = [
    path('', views.base, name='base'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup', SignUp.as_view(), name='signup'),
    path('add_librarian', AddLibrarian.as_view(), name='add_librarian'),
    path('add_student', AddStudent.as_view(), name='add_student'),
    path('add_book', AddBook.as_view(), name='add_book'),
    path('add_category', AddCategory.as_view(), name='add_category'),
    path('list_loaned', ListLoaned.as_view(), name='list_loaned'),
    path('list_books', ListBooks.as_view(template_name='list_books.html'), name='list_books'),
    path('view_book/<int:pk>/', ViewBook.as_view(template_name='view_book.html'), name='view_book'),
    path('delete_book/<int:pk>/', DeleteBook.as_view(template_name='delete_book.html'), name='delete_book'),
    path('edit_book/<int:pk>/', EditBook.as_view(template_name='edit_book.html'), name='edit_book'),
    path('search_author/', SearchByAuthor.as_view(), name='search_by_author'),
    path('search_title/', SearchByTitle.as_view(), name='search_by_title')
]