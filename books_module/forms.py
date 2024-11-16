from django.forms import ModelForm
from .models import Book

class Add_Book_Form(ModelForm):
    class Meta:
        model=Book
        fields=['title','price','author','publish_date','book_category']

