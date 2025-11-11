from django.test import TestCase
from django.urls import reverse 
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book
# Create your tests here.
class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
       cls.book = Book.objects.create(
        title="A good title",
        subtitle="An excellent subtitle",
        author="Tom Christie",
        isbn="1234567890123",
        )
    def  test_api_list_view(self):
        response = self.client.get(reverse('book-api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "A good title")