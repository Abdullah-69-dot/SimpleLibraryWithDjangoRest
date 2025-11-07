from django.contrib import admin
from django.urls import path
from books.views import ListBooks
urlpatterns = [
    path('', ListBooks.as_view(), name='book-list'),
]
