import json

from django.test import TestCase
from django.urls import reverse
from .models import Book,Book_Category
from datetime import datetime
import decimal
# Create your tests here.
class test1(TestCase):
    def setUp(self):
        self.category=Book_Category(title='cat')
        token_response=self.client.get(reverse('generate_token'))
        token=json.loads(token_response.content.decode('utf-8'))['token']
        self.assertEqual(token_response.status_code,200,msg='failed to generate csrf token')
        self.csrf_token=token

        auth_token_response=self.client.post(
            reverse('log_in'),headers={'X-csrftoken':self.csrf_token},data={'username':'admin','password':'1234'})
        self.assertEqual(auth_token_response.status_code, 200, msg='failed to authenticate')
        auth_token=json.loads(auth_token_response.content.decode('utf-8'))['token']
        self.auth_token=auth_token
        self.book=Book(title='title',book_category_id=self.category.id,publish_date=datetime(2022,5,2),author='author',price=22.56)
    def test(self):
        self.assertEqual(self.category.title,'cat',msg='failed to create book category')
        self.assertEqual(self.book.title,'title',msg='book title was not set correctly')
        books=self.client.get(reverse('show_all_books'))

        print(books)
