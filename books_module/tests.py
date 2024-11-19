from django.test import TestCase
from django.urls import reverse
from .models import Book,Book_Category
from datetime import datetime
import decimal
# Create your tests here.
class test1(TestCase):
    def setUp(self):
        self.category=Book_Category(title='cat')
        self.book=Book(title='title',book_category_id=self.category.id,publish_date=datetime(2022,5,2),author='author',price=22.56)
    def do(self):
        self.assertEqual(self.category.title,'cat',msg='failed to create book category')
        self.assertEqual(self.book.title,'title',ms='book title was not set correctly')
        books=self.client.get(reverse('show_all_books'))
        print(books)
