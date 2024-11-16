
from rest_framework import serializers
from .models import Book,Book_Category
class Books_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['title','price']


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Book_Category
        fields=['title']